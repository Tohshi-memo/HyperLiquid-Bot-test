# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T13:22:30.641067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.087` n `230`; crypto_major avg `0.0525` n `8`; equity avg `-0.1487` n `109`; fx avg `0.0034` n `6`; index avg `0.0004` n `25`; metal avg `0.0256` n `20`; unknown avg `0.0271` n `781`
- 1h: commodity avg `0.1122` n `12`; crypto_alt avg `-0.1694` n `230`; crypto_major avg `-0.4236` n `8`; equity avg `-0.5061` n `109`; fx avg `0.0094` n `6`; index avg `-0.0264` n `25`; metal avg `-0.1206` n `20`; unknown avg `-0.1255` n `781`
- 4h: commodity avg `0.2359` n `12`; crypto_alt avg `-0.1788` n `230`; crypto_major avg `-0.7973` n `8`; equity avg `-0.7345` n `109`; fx avg `0.0019` n `6`; index avg `-0.0782` n `25`; metal avg `-0.2911` n `20`; unknown avg `108.0708` n `781`
- 24h: commodity avg `0.0732` n `12`; crypto_alt avg `-0.0443` n `230`; crypto_major avg `-1.0424` n `8`; equity avg `-2.1479` n `109`; fx avg `0.0037` n `6`; index avg `-0.462` n `25`; metal avg `0.1978` n `20`; unknown avg `113.1589` n `749`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
