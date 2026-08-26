# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T17:07:27.415710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.1865` n `231`; crypto_major avg `0.1543` n `8`; equity avg `0.1003` n `122`; fx avg `0.0029` n `6`; index avg `0.0128` n `25`; metal avg `0.0306` n `20`; unknown avg `0.0902` n `797`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.2659` n `231`; crypto_major avg `-0.2748` n `8`; equity avg `0.0981` n `122`; fx avg `0.0006` n `6`; index avg `0.0094` n `25`; metal avg `-0.0353` n `20`; unknown avg `-0.0381` n `797`
- 4h: commodity avg `0.4662` n `12`; crypto_alt avg `-1.248` n `231`; crypto_major avg `-0.8782` n `8`; equity avg `0.2006` n `122`; fx avg `0.0053` n `6`; index avg `0.032` n `25`; metal avg `-0.2029` n `20`; unknown avg `-0.1631` n `797`
- 24h: commodity avg `0.3891` n `12`; crypto_alt avg `-2.201` n `231`; crypto_major avg `-2.0432` n `8`; equity avg `-0.3023` n `122`; fx avg `-0.0342` n `6`; index avg `0.0123` n `25`; metal avg `-0.2811` n `20`; unknown avg `0.5313` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
