# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T07:07:28.509489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.041` n `12`; crypto_alt avg `0.1483` n `231`; crypto_major avg `0.2462` n `8`; equity avg `-0.0791` n `122`; fx avg `0.0145` n `6`; index avg `-0.0109` n `25`; metal avg `0.0023` n `20`; unknown avg `0.1199` n `797`
- 1h: commodity avg `-0.109` n `12`; crypto_alt avg `-0.1459` n `231`; crypto_major avg `-0.129` n `8`; equity avg `0.0107` n `122`; fx avg `-0.003` n `6`; index avg `0.0069` n `25`; metal avg `-0.0875` n `20`; unknown avg `0.0831` n `797`
- 4h: commodity avg `0.0269` n `12`; crypto_alt avg `-0.1071` n `231`; crypto_major avg `0.1021` n `8`; equity avg `-0.1298` n `122`; fx avg `-0.0386` n `6`; index avg `-0.009` n `25`; metal avg `-0.1352` n `20`; unknown avg `0.148` n `781`
- 24h: commodity avg `-0.5915` n `12`; crypto_alt avg `-2.4046` n `231`; crypto_major avg `-2.468` n `8`; equity avg `0.5431` n `122`; fx avg `-0.0315` n `6`; index avg `0.0622` n `25`; metal avg `0.1268` n `20`; unknown avg `0.7876` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
