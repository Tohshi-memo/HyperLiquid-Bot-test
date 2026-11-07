# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T12:22:24.855475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `13`; crypto_alt avg `0.1039` n `239`; crypto_major avg `0.0004` n `8`; equity avg `0.0371` n `158`; fx avg `0.0442` n `6`; index avg `0.0019` n `27`; metal avg `0.0003` n `20`; unknown avg `0.1095` n `1261`
- 1h: commodity avg `-0.008` n `13`; crypto_alt avg `0.1899` n `239`; crypto_major avg `0.005` n `8`; equity avg `-0.0383` n `158`; fx avg `0.0378` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.2315` n `1249`
- 4h: commodity avg `0.0586` n `13`; crypto_alt avg `-0.5232` n `239`; crypto_major avg `-0.3813` n `8`; equity avg `-0.0919` n `158`; fx avg `0.0545` n `6`; index avg `-0.025` n `27`; metal avg `-0.0038` n `20`; unknown avg `43.1741` n `1209`
- 24h: commodity avg `-0.0576` n `13`; crypto_alt avg `-1.518` n `239`; crypto_major avg `-0.7828` n `8`; equity avg `-0.7252` n `158`; fx avg `-0.0343` n `6`; index avg `-0.0311` n `27`; metal avg `-0.0058` n `20`; unknown avg `-0.3754` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
