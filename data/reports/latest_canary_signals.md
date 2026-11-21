# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T14:52:33.796823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.1748` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1064` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3318` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0038` n `13`; crypto_alt avg `0.1176` n `239`; crypto_major avg `0.2425` n `8`; equity avg `0.0651` n `166`; fx avg `0.0015` n `6`; index avg `-0.0081` n `27`; metal avg `0.0141` n `20`; unknown avg `0.5325` n `1262`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `0.1538` n `239`; crypto_major avg `-0.1987` n `8`; equity avg `-0.2086` n `166`; fx avg `0.0075` n `6`; index avg `-0.0327` n `27`; metal avg `-0.0283` n `20`; unknown avg `4.9946` n `1260`
- 4h: commodity avg `0.0761` n `13`; crypto_alt avg `2.678` n `239`; crypto_major avg `3.2509` n `8`; equity avg `0.9191` n `166`; fx avg `0.0279` n `6`; index avg `0.0974` n `27`; metal avg `0.1445` n `20`; unknown avg `0.9309` n `1224`
- 24h: commodity avg `0.6552` n `13`; crypto_alt avg `-1.5205` n `239`; crypto_major avg `-1.5538` n `8`; equity avg `-3.4448` n `166`; fx avg `-0.0971` n `6`; index avg `-0.4083` n `27`; metal avg `-0.1814` n `20`; unknown avg `33.2937` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
