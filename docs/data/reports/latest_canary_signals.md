# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T22:07:25.530985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1996` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.4906` n `231`; crypto_major avg `0.4512` n `8`; equity avg `0.0387` n `122`; fx avg `-0.0171` n `6`; index avg `0.0086` n `25`; metal avg `0.0329` n `20`; unknown avg `0.0819` n `795`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `1.1324` n `231`; crypto_major avg `1.1027` n `8`; equity avg `0.22` n `122`; fx avg `-0.0036` n `6`; index avg `0.0116` n `25`; metal avg `0.0514` n `20`; unknown avg `0.5217` n `795`
- 4h: commodity avg `-0.1356` n `12`; crypto_alt avg `-1.2145` n `231`; crypto_major avg `-1.1214` n `8`; equity avg `0.3506` n `122`; fx avg `-0.0215` n `6`; index avg `0.0782` n `25`; metal avg `0.0787` n `20`; unknown avg `-0.2655` n `795`
- 24h: commodity avg `-0.6822` n `12`; crypto_alt avg `-1.9278` n `231`; crypto_major avg `-0.6746` n `8`; equity avg `2.0541` n `122`; fx avg `0.0428` n `6`; index avg `0.2651` n `25`; metal avg `-0.065` n `20`; unknown avg `-0.4648` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
