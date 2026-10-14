# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T13:07:30.829748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0156` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.4163` n `235`; crypto_major avg `-0.2797` n `8`; equity avg `-0.2711` n `151`; fx avg `-0.0212` n `6`; index avg `-0.0564` n `26`; metal avg `-0.1914` n `20`; unknown avg `-0.1638` n `1134`
- 1h: commodity avg `-0.131` n `13`; crypto_alt avg `-1.6852` n `235`; crypto_major avg `-1.2611` n `8`; equity avg `-1.2918` n `151`; fx avg `-0.104` n `6`; index avg `-0.2455` n `26`; metal avg `-0.4784` n `20`; unknown avg `2.6681` n `1134`
- 4h: commodity avg `-0.0663` n `13`; crypto_alt avg `-1.5287` n `235`; crypto_major avg `-0.8917` n `8`; equity avg `-1.3799` n `151`; fx avg `-0.0811` n `6`; index avg `-0.2468` n `26`; metal avg `-0.4179` n `20`; unknown avg `1.8008` n `1127`
- 24h: commodity avg `0.6237` n `13`; crypto_alt avg `-1.2199` n `235`; crypto_major avg `-0.5465` n `8`; equity avg `-0.9525` n `151`; fx avg `-0.0998` n `6`; index avg `-0.166` n `26`; metal avg `-0.6993` n `20`; unknown avg `1269.102` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1462`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1225`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
