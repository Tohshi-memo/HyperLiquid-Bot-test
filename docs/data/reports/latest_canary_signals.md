# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T17:52:31.224238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.1484` n `230`; crypto_major avg `-0.1969` n `8`; equity avg `0.0482` n `102`; fx avg `0.0045` n `6`; index avg `0.0146` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.1075` n `774`
- 1h: commodity avg `-0.1056` n `12`; crypto_alt avg `-0.0612` n `230`; crypto_major avg `-0.0107` n `8`; equity avg `-0.1603` n `102`; fx avg `-0.0241` n `6`; index avg `-0.0009` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.1605` n `774`
- 4h: commodity avg `-0.2789` n `12`; crypto_alt avg `-1.5281` n `230`; crypto_major avg `-1.3833` n `8`; equity avg `-2.0753` n `102`; fx avg `-0.1099` n `6`; index avg `-0.4417` n `25`; metal avg `-0.0976` n `20`; unknown avg `-0.4166` n `774`
- 24h: commodity avg `-0.7003` n `12`; crypto_alt avg `-1.1304` n `230`; crypto_major avg `-0.3306` n `8`; equity avg `-1.8042` n `102`; fx avg `-0.0065` n `6`; index avg `-0.521` n `25`; metal avg `0.1978` n `20`; unknown avg `-0.4299` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
