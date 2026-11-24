# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T15:46:44.211526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3757` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0896` n `13`; crypto_alt avg `-0.2459` n `239`; crypto_major avg `-0.2609` n `8`; equity avg `-0.6255` n `168`; fx avg `-0.0011` n `6`; index avg `-0.0558` n `27`; metal avg `-0.0378` n `20`; unknown avg `155.1442` n `1263`
- 1h: commodity avg `-0.2825` n `13`; crypto_alt avg `-1.3398` n `239`; crypto_major avg `-1.1699` n `8`; equity avg `-2.1465` n `168`; fx avg `-0.0027` n `6`; index avg `-0.2019` n `27`; metal avg `-0.5065` n `20`; unknown avg `-0.2876` n `1257`
- 4h: commodity avg `0.0898` n `13`; crypto_alt avg `-1.6928` n `239`; crypto_major avg `-1.5568` n `8`; equity avg `-2.2722` n `167`; fx avg `0.0433` n `6`; index avg `-0.1811` n `27`; metal avg `-0.4446` n `20`; unknown avg `161.2508` n `1241`
- 24h: commodity avg `0.4438` n `13`; crypto_alt avg `-5.2446` n `239`; crypto_major avg `-5.7023` n `8`; equity avg `-5.1119` n `167`; fx avg `0.1902` n `6`; index avg `-0.379` n `27`; metal avg `-1.1324` n `20`; unknown avg `-0.7166` n `1135`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
