# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T11:22:29.017244+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0475` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.2705` n `235`; crypto_major avg `-0.1712` n `8`; equity avg `-0.031` n `150`; fx avg `-0.0012` n `6`; index avg `-0.0083` n `26`; metal avg `0.0137` n `20`; unknown avg `1.3324` n `1076`
- 1h: commodity avg `0.1558` n `13`; crypto_alt avg `-0.5792` n `235`; crypto_major avg `-0.401` n `8`; equity avg `-0.3553` n `150`; fx avg `0.0067` n `6`; index avg `-0.0598` n `26`; metal avg `0.0025` n `20`; unknown avg `0.3293` n `1074`
- 4h: commodity avg `0.2819` n `13`; crypto_alt avg `-1.6496` n `235`; crypto_major avg `-1.1987` n `8`; equity avg `-0.9792` n `150`; fx avg `-0.0665` n `6`; index avg `-0.1512` n `26`; metal avg `-0.2412` n `20`; unknown avg `2.1243` n `1058`
- 24h: commodity avg `1.4149` n `13`; crypto_alt avg `-5.2358` n `235`; crypto_major avg `-3.5701` n `8`; equity avg `-1.5865` n `150`; fx avg `-0.1351` n `6`; index avg `-0.342` n `26`; metal avg `-0.5298` n `20`; unknown avg `815.8205` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
