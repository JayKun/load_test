val fileRdd = sc.textFile("twitter.edges")

val splitRdd = fileRdd.map( line => line.split(": "))

val yourRdd = splitRdd.flatMap( arr => {
    val user = arr(0)
    val users = arr(1).split(",")
    users.map( followed => (followed, 1))
})

val reducedRdd = yourRdd.reduceByKey((a,b) => a+b)

val res = reducedRdd.filter((e) => (e._2 > 1000))

res.saveAsTextFile("output")

System.exit(0)
