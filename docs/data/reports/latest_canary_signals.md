# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T10:51:27.348997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.096` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0207` n `228`; crypto_major avg `-0.1646` n `8`; equity avg `-0.0461` n `86`; fx avg `0.002` n `6`; index avg `0.0224` n `23`; metal avg `-0.056` n `20`; unknown avg `-0.0473` n `765`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `-0.3955` n `228`; crypto_major avg `-0.5954` n `8`; equity avg `0.1119` n `86`; fx avg `-0.0324` n `6`; index avg `0.0464` n `23`; metal avg `-0.1002` n `20`; unknown avg `-0.0692` n `765`
- 4h: commodity avg `0.0873` n `12`; crypto_alt avg `-0.672` n `228`; crypto_major avg `-1.0503` n `8`; equity avg `0.217` n `86`; fx avg `-0.0025` n `6`; index avg `0.0457` n `23`; metal avg `0.2674` n `20`; unknown avg `-0.0049` n `749`
- 24h: commodity avg `-0.255` n `12`; crypto_alt avg `-1.211` n `228`; crypto_major avg `-1.081` n `8`; equity avg `0.2314` n `86`; fx avg `-0.006` n `6`; index avg `0.5145` n `23`; metal avg `-1.1325` n `20`; unknown avg `-0.5328` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
