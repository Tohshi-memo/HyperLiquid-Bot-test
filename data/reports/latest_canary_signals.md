# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T12:07:26.798374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0415` n `13`; crypto_alt avg `-0.1735` n `236`; crypto_major avg `-0.2905` n `8`; equity avg `0.1911` n `151`; fx avg `-0.0087` n `6`; index avg `0.0439` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.2091` n `1128`
- 1h: commodity avg `0.0239` n `13`; crypto_alt avg `0.1609` n `236`; crypto_major avg `-0.1155` n `8`; equity avg `-0.0289` n `151`; fx avg `0.0009` n `6`; index avg `0.0121` n `26`; metal avg `-0.0019` n `20`; unknown avg `21.1483` n `1128`
- 4h: commodity avg `0.074` n `13`; crypto_alt avg `0.3123` n `236`; crypto_major avg `0.1444` n `8`; equity avg `-0.4347` n `151`; fx avg `0.0417` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.8928` n `1104`
- 24h: commodity avg `0.0021` n `13`; crypto_alt avg `4.6193` n `236`; crypto_major avg `2.5664` n `8`; equity avg `2.4066` n `151`; fx avg `0.0176` n `6`; index avg `0.3295` n `26`; metal avg `0.3128` n `20`; unknown avg `25.3308` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0961`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0892`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
