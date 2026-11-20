# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T04:52:37.134145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.254` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0741` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0193` n `13`; crypto_alt avg `0.2046` n `239`; crypto_major avg `0.1389` n `8`; equity avg `-0.0394` n `165`; fx avg `-0.0021` n `6`; index avg `0.0139` n `27`; metal avg `0.042` n `20`; unknown avg `0.2473` n `1260`
- 1h: commodity avg `-0.0379` n `13`; crypto_alt avg `-0.7638` n `239`; crypto_major avg `-1.1249` n `8`; equity avg `-0.7373` n `165`; fx avg `-0.0056` n `6`; index avg `-0.0508` n `27`; metal avg `-0.218` n `20`; unknown avg `-0.3665` n `1242`
- 4h: commodity avg `0.0148` n `13`; crypto_alt avg `-1.8083` n `239`; crypto_major avg `-1.2617` n `8`; equity avg `-0.5132` n `165`; fx avg `-0.013` n `6`; index avg `-0.0077` n `27`; metal avg `-0.6387` n `20`; unknown avg `1.9507` n `1244`
- 24h: commodity avg `-0.0081` n `13`; crypto_alt avg `-3.7579` n `239`; crypto_major avg `-3.0511` n `8`; equity avg `-5.8259` n `165`; fx avg `0.0264` n `6`; index avg `-0.4846` n `27`; metal avg `-1.7106` n `20`; unknown avg `391.742` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
