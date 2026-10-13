# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T12:22:25.808423+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4264` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `-0.2244` n `235`; crypto_major avg `-0.202` n `8`; equity avg `-0.1416` n `151`; fx avg `0.0004` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0755` n `20`; unknown avg `-0.1399` n `1135`
- 1h: commodity avg `0.0474` n `13`; crypto_alt avg `-0.7045` n `235`; crypto_major avg `-0.6178` n `8`; equity avg `-0.2822` n `151`; fx avg `0.0178` n `6`; index avg `-0.0065` n `26`; metal avg `-0.1067` n `20`; unknown avg `-0.2314` n `1127`
- 4h: commodity avg `0.0874` n `13`; crypto_alt avg `-2.2491` n `235`; crypto_major avg `-1.496` n `8`; equity avg `-0.9012` n `151`; fx avg `-0.0031` n `6`; index avg `-0.0696` n `26`; metal avg `-0.1726` n `20`; unknown avg `0.2215` n `1127`
- 24h: commodity avg `0.0219` n `13`; crypto_alt avg `-4.836` n `235`; crypto_major avg `-2.5223` n `8`; equity avg `-3.3514` n `151`; fx avg `0.0887` n `6`; index avg `-0.3945` n `26`; metal avg `-0.0712` n `20`; unknown avg `0.1549` n `990`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1697`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1689`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1488`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1469`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0871`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
