# THEANO_FLAGS=device=gpu,nvcc.flags=-D_FORCE_INLINES,-arch=sm_52 ipython2 -c "import theano; print(theano.sandbox.cuda.device_properties(0))"
# THEANO_FLAGS=device=gpu ipython2 -c "import theano; print(theano.sandbox.cuda.device_properties(0))"


# python -c "from theano.sandbox.cuda.dnn import dnn_available as d; print(d() or d.msg)"

THEANO_FLAGS=device=gpu ./tweet2vec_trainer.sh
THEANO_FLAGS=device=gpu ./tweet2vec_tester.sh