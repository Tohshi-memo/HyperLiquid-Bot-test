# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T05:37:28.855855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `13`; crypto_alt avg `-0.2999` n `235`; crypto_major avg `-0.1177` n `8`; equity avg `-0.1929` n `151`; fx avg `0.0198` n `6`; index avg `-0.0302` n `26`; metal avg `0.0038` n `20`; unknown avg `-0.2413` n `1135`
- 1h: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.8566` n `235`; crypto_major avg `-0.5267` n `8`; equity avg `-0.4916` n `151`; fx avg `0.008` n `6`; index avg `-0.0817` n `26`; metal avg `-0.0233` n `20`; unknown avg `-0.1923` n `1133`
- 4h: commodity avg `-0.185` n `13`; crypto_alt avg `-0.1154` n `235`; crypto_major avg `0.0739` n `8`; equity avg `-0.2771` n `151`; fx avg `-0.0158` n `6`; index avg `-0.0156` n `26`; metal avg `0.179` n `20`; unknown avg `-0.4599` n `1127`
- 24h: commodity avg `0.9808` n `13`; crypto_alt avg `-1.0509` n `235`; crypto_major avg `-0.3962` n `8`; equity avg `-0.1293` n `151`; fx avg `0.0493` n `6`; index avg `0.056` n `26`; metal avg `-0.3402` n `20`; unknown avg `0.8795` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1546`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0829`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0738`, n `666`, weak_sample_signal
