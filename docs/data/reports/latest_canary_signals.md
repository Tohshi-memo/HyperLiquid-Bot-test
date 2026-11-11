# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T23:22:29.637413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5971` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5893` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.3757` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0124` n `13`; crypto_alt avg `-0.5867` n `239`; crypto_major avg `-0.4601` n `8`; equity avg `-0.2496` n `161`; fx avg `-0.0007` n `6`; index avg `-0.023` n `27`; metal avg `-0.0302` n `20`; unknown avg `1.5548` n `1262`
- 1h: commodity avg `-0.0402` n `13`; crypto_alt avg `-1.9336` n `239`; crypto_major avg `-1.6761` n `8`; equity avg `-1.2714` n `161`; fx avg `-0.0066` n `6`; index avg `-0.0868` n `27`; metal avg `-0.079` n `20`; unknown avg `3.7182` n `1256`
- 4h: commodity avg `-0.1391` n `13`; crypto_alt avg `-1.9085` n `239`; crypto_major avg `-1.5406` n `8`; equity avg `-1.9081` n `161`; fx avg `-0.0279` n `6`; index avg `-0.1649` n `27`; metal avg `-0.1032` n `20`; unknown avg `5.8338` n `1204`
- 24h: commodity avg `0.217` n `13`; crypto_alt avg `-1.7478` n `239`; crypto_major avg `-0.6688` n `8`; equity avg `2.3729` n `161`; fx avg `-0.1633` n `6`; index avg `0.2867` n `27`; metal avg `-0.1615` n `20`; unknown avg `4.0374` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
