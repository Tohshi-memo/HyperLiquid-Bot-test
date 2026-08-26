# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T04:07:13.860398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `0.0284` n `231`; crypto_major avg `0.1064` n `8`; equity avg `-0.0038` n `122`; fx avg `-0.0183` n `6`; index avg `-0.0198` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0806` n `797`
- 1h: commodity avg `0.0127` n `12`; crypto_alt avg `-0.1994` n `231`; crypto_major avg `-0.048` n `8`; equity avg `0.1849` n `122`; fx avg `-0.0381` n `6`; index avg `0.0224` n `25`; metal avg `-0.0309` n `20`; unknown avg `-0.1074` n `797`
- 4h: commodity avg `-0.0828` n `12`; crypto_alt avg `1.1442` n `231`; crypto_major avg `0.933` n `8`; equity avg `0.4617` n `122`; fx avg `-0.0429` n `6`; index avg `0.1504` n `25`; metal avg `0.0759` n `20`; unknown avg `0.6293` n `796`
- 24h: commodity avg `-0.8759` n `12`; crypto_alt avg `-2.4129` n `231`; crypto_major avg `-2.3678` n `8`; equity avg `1.4638` n `122`; fx avg `0.0001` n `6`; index avg `0.2019` n `25`; metal avg `0.268` n `20`; unknown avg `0.0841` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
