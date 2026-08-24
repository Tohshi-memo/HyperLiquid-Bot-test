# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:07:26.079419+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.2743` n `231`; crypto_major avg `-0.1` n `8`; equity avg `0.0113` n `122`; fx avg `-0.001` n `6`; index avg `-0.0026` n `25`; metal avg `0.0095` n `20`; unknown avg `0.4688` n `794`
- 1h: commodity avg `0.0154` n `12`; crypto_alt avg `-0.4355` n `231`; crypto_major avg `-0.2141` n `8`; equity avg `-0.0583` n `122`; fx avg `0.0008` n `6`; index avg `-0.0034` n `25`; metal avg `0.0514` n `20`; unknown avg `0.485` n `794`
- 4h: commodity avg `-0.0979` n `12`; crypto_alt avg `0.2013` n `231`; crypto_major avg `0.5094` n `8`; equity avg `-0.2803` n `122`; fx avg `-0.0118` n `6`; index avg `-0.042` n `25`; metal avg `0.1658` n `20`; unknown avg `-0.5396` n `794`
- 24h: commodity avg `-0.105` n `12`; crypto_alt avg `-1.7723` n `231`; crypto_major avg `-0.8816` n `8`; equity avg `-2.8157` n `122`; fx avg `-0.0614` n `6`; index avg `-0.3412` n `25`; metal avg `0.2679` n `20`; unknown avg `0.832` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
