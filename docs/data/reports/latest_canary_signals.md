# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T19:22:31.145796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0571` n `230`; crypto_major avg `-0.05` n `8`; equity avg `0.0516` n `98`; fx avg `0.0053` n `6`; index avg `-0.0004` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0681` n `771`
- 1h: commodity avg `0.107` n `12`; crypto_alt avg `0.0303` n `230`; crypto_major avg `-0.1162` n `8`; equity avg `-0.2035` n `98`; fx avg `0.0097` n `6`; index avg `-0.0153` n `25`; metal avg `0.0557` n `20`; unknown avg `-0.0316` n `771`
- 4h: commodity avg `0.0885` n `12`; crypto_alt avg `-0.1393` n `230`; crypto_major avg `-0.5245` n `8`; equity avg `0.04` n `98`; fx avg `0.0299` n `6`; index avg `0.0386` n `25`; metal avg `0.0138` n `20`; unknown avg `-0.0387` n `771`
- 24h: commodity avg `0.3555` n `12`; crypto_alt avg `0.9765` n `230`; crypto_major avg `0.7844` n `8`; equity avg `3.5857` n `98`; fx avg `0.0477` n `6`; index avg `0.6281` n `25`; metal avg `0.7539` n `20`; unknown avg `0.3458` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0892`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.053`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
