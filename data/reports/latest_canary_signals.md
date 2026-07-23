# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T16:52:30.063865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `12`; crypto_alt avg `-0.0006` n `230`; crypto_major avg `0.005` n `8`; equity avg `-0.1605` n `100`; fx avg `0.0041` n `6`; index avg `-0.0509` n `25`; metal avg `0.0144` n `20`; unknown avg `-0.0575` n `772`
- 1h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.158` n `230`; crypto_major avg `-0.4034` n `8`; equity avg `0.5595` n `100`; fx avg `0.0107` n `6`; index avg `0.086` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.1229` n `772`
- 4h: commodity avg `0.0547` n `12`; crypto_alt avg `-0.5098` n `230`; crypto_major avg `-0.9613` n `8`; equity avg `0.0756` n `100`; fx avg `-0.0148` n `6`; index avg `-0.0791` n `25`; metal avg `-0.1531` n `20`; unknown avg `-0.24` n `772`
- 24h: commodity avg `1.0587` n `12`; crypto_alt avg `-1.6232` n `230`; crypto_major avg `-2.2436` n `8`; equity avg `-1.3684` n `99`; fx avg `-0.0682` n `6`; index avg `-0.3611` n `25`; metal avg `-0.8307` n `20`; unknown avg `-0.2099` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0679`, n `666`, weak_sample_signal
