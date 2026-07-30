# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T13:22:27.819101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.303` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `-0.0379` n `230`; crypto_major avg `-0.1087` n `8`; equity avg `-0.0761` n `102`; fx avg `-0.0052` n `6`; index avg `-0.0154` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.004` n `779`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `-0.1061` n `230`; crypto_major avg `-0.1213` n `8`; equity avg `0.8249` n `102`; fx avg `-0.0289` n `6`; index avg `0.1284` n `25`; metal avg `0.0249` n `20`; unknown avg `-0.0127` n `779`
- 4h: commodity avg `-0.2424` n `12`; crypto_alt avg `-0.1019` n `230`; crypto_major avg `0.064` n `8`; equity avg `2.367` n `102`; fx avg `-0.0958` n `6`; index avg `0.3511` n `25`; metal avg `0.1077` n `20`; unknown avg `0.0963` n `779`
- 24h: commodity avg `-0.0794` n `12`; crypto_alt avg `0.1793` n `230`; crypto_major avg `0.2981` n `8`; equity avg `-0.3467` n `102`; fx avg `-0.0774` n `6`; index avg `-0.0483` n `25`; metal avg `0.54` n `20`; unknown avg `-0.2586` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
