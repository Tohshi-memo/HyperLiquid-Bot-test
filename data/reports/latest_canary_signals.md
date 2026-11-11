# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T23:37:27.993213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0796` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `0.5709` n `239`; crypto_major avg `0.4765` n `8`; equity avg `0.4028` n `161`; fx avg `-0.0025` n `6`; index avg `0.0426` n `27`; metal avg `-0.0225` n `20`; unknown avg `2.5909` n `1262`
- 1h: commodity avg `-0.0252` n `13`; crypto_alt avg `-0.6276` n `239`; crypto_major avg `-0.6026` n `8`; equity avg `-0.2826` n `161`; fx avg `-0.003` n `6`; index avg `0.0227` n `27`; metal avg `-0.0881` n `20`; unknown avg `1.4766` n `1256`
- 4h: commodity avg `0.0738` n `13`; crypto_alt avg `-1.4068` n `239`; crypto_major avg `-1.2108` n `8`; equity avg `-1.622` n `161`; fx avg `-0.0283` n `6`; index avg `-0.1312` n `27`; metal avg `-0.1815` n `20`; unknown avg `5.1044` n `1204`
- 24h: commodity avg `0.1921` n `13`; crypto_alt avg `-1.2822` n `239`; crypto_major avg `-0.3187` n `8`; equity avg `2.728` n `161`; fx avg `-0.1816` n `6`; index avg `0.3286` n `27`; metal avg `-0.1892` n `20`; unknown avg `4.0815` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
