# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T01:22:24.277518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.7805` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2582` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1683` n `13`; crypto_alt avg `0.1547` n `239`; crypto_major avg `0.0394` n `8`; equity avg `-0.245` n `158`; fx avg `-0.022` n `6`; index avg `-0.0545` n `27`; metal avg `0.2566` n `20`; unknown avg `1.8121` n `1264`
- 1h: commodity avg `-0.0664` n `13`; crypto_alt avg `-0.3514` n `239`; crypto_major avg `-0.371` n `8`; equity avg `-1.4258` n `158`; fx avg `-0.0097` n `6`; index avg `-0.2573` n `27`; metal avg `0.1036` n `20`; unknown avg `0.9665` n `1258`
- 4h: commodity avg `-0.1658` n `13`; crypto_alt avg `-1.351` n `239`; crypto_major avg `-1.6177` n `8`; equity avg `-2.214` n `158`; fx avg `0.0098` n `6`; index avg `-0.3595` n `27`; metal avg `0.1628` n `20`; unknown avg `173.0849` n `1196`
- 24h: commodity avg `0.156` n `13`; crypto_alt avg `-0.1666` n `239`; crypto_major avg `-0.4414` n `8`; equity avg `-0.2832` n `158`; fx avg `0.1429` n `6`; index avg `-0.2165` n `27`; metal avg `-0.38` n `20`; unknown avg `3.7792` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
