# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T15:52:35.917922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.363` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1426` n `13`; crypto_alt avg `0.1077` n `238`; crypto_major avg `-0.0129` n `8`; equity avg `0.0525` n `155`; fx avg `0.0011` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0124` n `20`; unknown avg `1.4937` n `1238`
- 1h: commodity avg `0.1635` n `13`; crypto_alt avg `0.2681` n `238`; crypto_major avg `0.0164` n `8`; equity avg `0.3635` n `155`; fx avg `0.0204` n `6`; index avg `0.0445` n `27`; metal avg `0.0102` n `20`; unknown avg `-0.2956` n `1232`
- 4h: commodity avg `0.318` n `13`; crypto_alt avg `-1.1019` n `238`; crypto_major avg `-1.338` n `8`; equity avg `-0.5235` n `155`; fx avg `0.0922` n `6`; index avg `0.025` n `27`; metal avg `-0.0784` n `20`; unknown avg `1.9931` n `1152`
- 24h: commodity avg `0.6356` n `13`; crypto_alt avg `0.0264` n `238`; crypto_major avg `-0.0402` n `8`; equity avg `1.1791` n `154`; fx avg `0.2231` n `6`; index avg `0.2275` n `27`; metal avg `-0.2044` n `20`; unknown avg `3.4936` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
