# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T07:07:23.400186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0525` n `231`; crypto_major avg `0.0796` n `8`; equity avg `0.0342` n `122`; fx avg `0.0296` n `6`; index avg `0.0142` n `25`; metal avg `-0.0362` n `20`; unknown avg `-0.0467` n `793`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `0.1006` n `231`; crypto_major avg `0.5589` n `8`; equity avg `0.0974` n `122`; fx avg `0.0593` n `6`; index avg `0.0088` n `25`; metal avg `0.0336` n `20`; unknown avg `-0.0287` n `793`
- 4h: commodity avg `-0.0613` n `12`; crypto_alt avg `0.1553` n `231`; crypto_major avg `0.322` n `8`; equity avg `-0.4161` n `122`; fx avg `0.0342` n `6`; index avg `-0.0918` n `25`; metal avg `0.0958` n `20`; unknown avg `-0.0599` n `777`
- 24h: commodity avg `-0.3514` n `12`; crypto_alt avg `3.5583` n `231`; crypto_major avg `1.8541` n `8`; equity avg `-1.1404` n `122`; fx avg `-0.1625` n `6`; index avg `-0.1136` n `25`; metal avg `0.2192` n `20`; unknown avg `5.4304` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
