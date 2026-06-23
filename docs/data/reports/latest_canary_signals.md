# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T11:22:42.237531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1882` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `0.3516` n `228`; crypto_major avg `0.3032` n `8`; equity avg `0.1148` n `86`; fx avg `0.0031` n `6`; index avg `0.0082` n `23`; metal avg `0.0394` n `20`; unknown avg `0.0915` n `764`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `0.2607` n `228`; crypto_major avg `0.2989` n `8`; equity avg `0.0715` n `86`; fx avg `0.0106` n `6`; index avg `-0.0543` n `23`; metal avg `-0.1293` n `20`; unknown avg `-0.0042` n `764`
- 4h: commodity avg `0.1587` n `12`; crypto_alt avg `-0.8368` n `228`; crypto_major avg `-1.2798` n `8`; equity avg `-0.3261` n `86`; fx avg `-0.0705` n `6`; index avg `-0.0916` n `23`; metal avg `-0.0834` n `20`; unknown avg `-0.4781` n `620`
- 24h: commodity avg `-0.5763` n `12`; crypto_alt avg `-3.9121` n `228`; crypto_major avg `-4.0146` n `8`; equity avg `-4.2711` n `85`; fx avg `-0.1179` n `6`; index avg `-0.9146` n `23`; metal avg `-1.299` n `20`; unknown avg `0.0531` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
