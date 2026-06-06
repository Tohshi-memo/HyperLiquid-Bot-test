# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T18:37:24.842248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0716` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `0.1624` n `228`; crypto_major avg `0.0884` n `8`; equity avg `0.049` n `74`; fx avg `-0.0208` n `6`; index avg `-0.0183` n `23`; metal avg `0.0162` n `18`; unknown avg `-0.118` n `515`
- 1h: commodity avg `-0.0713` n `12`; crypto_alt avg `0.1044` n `228`; crypto_major avg `-0.1128` n `8`; equity avg `0.0011` n `74`; fx avg `0.1491` n `6`; index avg `-0.0261` n `23`; metal avg `-0.0061` n `18`; unknown avg `3.6591` n `515`
- 4h: commodity avg `0.1011` n `12`; crypto_alt avg `-0.9889` n `228`; crypto_major avg `-1.1585` n `8`; equity avg `-0.1777` n `74`; fx avg `0.2134` n `6`; index avg `-0.0869` n `23`; metal avg `0.0991` n `18`; unknown avg `-3.4881` n `515`
- 24h: commodity avg `0.2415` n `12`; crypto_alt avg `-0.2728` n `228`; crypto_major avg `-0.0585` n `8`; equity avg `-0.948` n `74`; fx avg `0.174` n `6`; index avg `-0.7022` n `23`; metal avg `-0.6693` n `18`; unknown avg `0.8373` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
