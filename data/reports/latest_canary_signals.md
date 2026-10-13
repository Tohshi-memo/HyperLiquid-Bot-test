# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T16:07:44.887966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0834` n `13`; crypto_alt avg `0.5388` n `235`; crypto_major avg `0.3242` n `8`; equity avg `0.3368` n `151`; fx avg `-0.0059` n `6`; index avg `0.0502` n `26`; metal avg `-0.0283` n `20`; unknown avg `0.624` n `1127`
- 1h: commodity avg `0.1062` n `13`; crypto_alt avg `-0.1629` n `235`; crypto_major avg `-0.072` n `8`; equity avg `0.1648` n `151`; fx avg `-0.0072` n `6`; index avg `0.0191` n `26`; metal avg `-0.0872` n `20`; unknown avg `0.5953` n `1123`
- 4h: commodity avg `0.7309` n `13`; crypto_alt avg `0.813` n `235`; crypto_major avg `0.6143` n `8`; equity avg `0.2311` n `151`; fx avg `0.0322` n `6`; index avg `0.0121` n `26`; metal avg `-0.3496` n `20`; unknown avg `0.4299` n `1091`
- 24h: commodity avg `0.3861` n `13`; crypto_alt avg `-2.3382` n `235`; crypto_major avg `-0.9439` n `8`; equity avg `-1.6085` n `151`; fx avg `0.1516` n `6`; index avg `-0.2943` n `26`; metal avg `-0.264` n `20`; unknown avg `-0.15` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1641`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.149`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1318`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0938`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
