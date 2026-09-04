# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T16:07:24.985405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.8503` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.4843` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3239` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.11` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.0424` n `232`; crypto_major avg `-0.0221` n `8`; equity avg `0.1092` n `133`; fx avg `-0.0021` n `6`; index avg `0.0098` n `26`; metal avg `-0.0552` n `20`; unknown avg `-0.0809` n `791`
- 1h: commodity avg `0.0643` n `12`; crypto_alt avg `0.5148` n `232`; crypto_major avg `0.3908` n `8`; equity avg `0.2171` n `133`; fx avg `0.0051` n `6`; index avg `0.0368` n `26`; metal avg `-0.0148` n `20`; unknown avg `0.0502` n `779`
- 4h: commodity avg `0.2243` n `12`; crypto_alt avg `-1.5899` n `232`; crypto_major avg `-2.26` n `8`; equity avg `0.5903` n `133`; fx avg `-0.0746` n `6`; index avg `0.0639` n `26`; metal avg `-0.15` n `20`; unknown avg `0.5541` n `725`
- 24h: commodity avg `0.1387` n `12`; crypto_alt avg `-1.1733` n `232`; crypto_major avg `-1.826` n `8`; equity avg `1.587` n `133`; fx avg `-0.0704` n `6`; index avg `0.1948` n `26`; metal avg `-0.2952` n `20`; unknown avg `27.5882` n `686`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
