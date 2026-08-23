# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T21:37:25.712402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.174` n `231`; crypto_major avg `-0.1552` n `8`; equity avg `-0.0069` n `122`; fx avg `0.0018` n `6`; index avg `0.0012` n `25`; metal avg `-0.0192` n `20`; unknown avg `0.1187` n `793`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.769` n `231`; crypto_major avg `0.8559` n `8`; equity avg `0.0637` n `122`; fx avg `-0.0331` n `6`; index avg `0.0037` n `25`; metal avg `-0.016` n `20`; unknown avg `1.3532` n `793`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.9438` n `231`; crypto_major avg `0.9665` n `8`; equity avg `0.2434` n `122`; fx avg `-0.116` n `6`; index avg `0.049` n `25`; metal avg `0.0354` n `20`; unknown avg `3.0935` n `793`
- 24h: commodity avg `-0.1472` n `12`; crypto_alt avg `4.8016` n `231`; crypto_major avg `2.3085` n `8`; equity avg `0.8595` n `122`; fx avg `-0.1042` n `6`; index avg `0.1336` n `25`; metal avg `0.0828` n `20`; unknown avg `8.5341` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
