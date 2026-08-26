# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T06:07:23.277088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `0.1131` n `231`; crypto_major avg `0.1299` n `8`; equity avg `-0.1042` n `122`; fx avg `0.0057` n `6`; index avg `-0.0082` n `25`; metal avg `-0.0041` n `20`; unknown avg `0.0103` n `781`
- 1h: commodity avg `0.0885` n `12`; crypto_alt avg `0.6717` n `231`; crypto_major avg `0.7545` n `8`; equity avg `-0.2188` n `122`; fx avg `0.0017` n `6`; index avg `-0.025` n `25`; metal avg `0.003` n `20`; unknown avg `0.0858` n `781`
- 4h: commodity avg `0.1346` n `12`; crypto_alt avg `0.5936` n `231`; crypto_major avg `0.627` n `8`; equity avg `0.4641` n `122`; fx avg `0.0217` n `6`; index avg `0.1171` n `25`; metal avg `-0.0822` n `20`; unknown avg `1.0761` n `781`
- 24h: commodity avg `-0.4761` n `12`; crypto_alt avg `-2.6394` n `231`; crypto_major avg `-2.4607` n `8`; equity avg `0.6012` n `122`; fx avg `0.0179` n `6`; index avg `0.0952` n `25`; metal avg `0.2051` n `20`; unknown avg `0.6316` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
