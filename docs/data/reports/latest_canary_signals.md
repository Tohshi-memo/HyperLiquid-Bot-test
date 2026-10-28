# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T12:37:26.809393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0528` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0684` n `13`; crypto_alt avg `-0.2589` n `238`; crypto_major avg `-0.2736` n `8`; equity avg `-0.0797` n `154`; fx avg `-0.0121` n `6`; index avg `-0.017` n `27`; metal avg `0.0269` n `20`; unknown avg `0.1582` n `1239`
- 1h: commodity avg `0.0128` n `13`; crypto_alt avg `-1.1232` n `238`; crypto_major avg `-0.9931` n `8`; equity avg `-0.3155` n `154`; fx avg `0.0293` n `6`; index avg `-0.0091` n `27`; metal avg `0.0801` n `20`; unknown avg `0.7283` n `1227`
- 4h: commodity avg `0.149` n `13`; crypto_alt avg `-0.9358` n `238`; crypto_major avg `-1.0323` n `8`; equity avg `-0.1583` n `154`; fx avg `0.056` n `6`; index avg `0.0205` n `27`; metal avg `0.0723` n `20`; unknown avg `1.1428` n `1196`
- 24h: commodity avg `0.1751` n `13`; crypto_alt avg `0.7984` n `238`; crypto_major avg `1.0083` n `8`; equity avg `2.5672` n `154`; fx avg `0.126` n `6`; index avg `0.3756` n `27`; metal avg `0.2936` n `20`; unknown avg `7.7308` n `1068`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
