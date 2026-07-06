# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T20:37:30.002275+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.1038` n `229`; crypto_major avg `0.2383` n `8`; equity avg `0.0114` n `91`; fx avg `0.0028` n `6`; index avg `-0.0008` n `25`; metal avg `0.0176` n `20`; unknown avg `0.1124` n `763`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.1544` n `229`; crypto_major avg `-0.1542` n `8`; equity avg `-0.0419` n `91`; fx avg `0.0068` n `6`; index avg `-0.0199` n `25`; metal avg `-0.0015` n `20`; unknown avg `-0.1372` n `763`
- 4h: commodity avg `0.1227` n `12`; crypto_alt avg `-0.1114` n `229`; crypto_major avg `0.0372` n `8`; equity avg `-0.5295` n `91`; fx avg `0.0068` n `6`; index avg `-0.0483` n `25`; metal avg `0.2088` n `20`; unknown avg `-0.2908` n `763`
- 24h: commodity avg `0.076` n `12`; crypto_alt avg `0.902` n `229`; crypto_major avg `0.7196` n `8`; equity avg `-0.6574` n `90`; fx avg `0.2149` n `6`; index avg `0.0251` n `25`; metal avg `-0.2072` n `20`; unknown avg `0.2497` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
