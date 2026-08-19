# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T03:22:29.965099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `0.3156` n `230`; crypto_major avg `0.1922` n `8`; equity avg `-0.0484` n `120`; fx avg `-0.0019` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.1393` n `789`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.2425` n `230`; crypto_major avg `0.1047` n `8`; equity avg `-0.2397` n `120`; fx avg `-0.0446` n `6`; index avg `-0.015` n `25`; metal avg `-0.0427` n `20`; unknown avg `-0.3038` n `789`
- 4h: commodity avg `0.0343` n `12`; crypto_alt avg `0.1714` n `230`; crypto_major avg `-0.2237` n `8`; equity avg `0.2458` n `120`; fx avg `-0.1573` n `6`; index avg `-0.078` n `25`; metal avg `0.0875` n `20`; unknown avg `-0.1844` n `789`
- 24h: commodity avg `0.3199` n `12`; crypto_alt avg `0.8284` n `230`; crypto_major avg `0.4322` n `8`; equity avg `-2.7409` n `120`; fx avg `-0.1304` n `6`; index avg `-0.4801` n `25`; metal avg `-0.5433` n `20`; unknown avg `-0.1249` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
