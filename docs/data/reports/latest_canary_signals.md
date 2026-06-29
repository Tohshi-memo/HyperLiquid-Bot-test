# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T01:52:30.201048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.2575` n `228`; crypto_major avg `0.2874` n `8`; equity avg `0.083` n `88`; fx avg `0.017` n `6`; index avg `0.0175` n `23`; metal avg `-0.0369` n `20`; unknown avg `-0.0618` n `764`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `0.4529` n `228`; crypto_major avg `0.4115` n `8`; equity avg `0.2835` n `88`; fx avg `0.0328` n `6`; index avg `0.0895` n `23`; metal avg `-0.058` n `20`; unknown avg `-0.0405` n `764`
- 4h: commodity avg `-0.1883` n `12`; crypto_alt avg `0.8704` n `228`; crypto_major avg `0.6746` n `8`; equity avg `-0.3079` n `88`; fx avg `0.0848` n `6`; index avg `-0.133` n `23`; metal avg `-0.2616` n `20`; unknown avg `1.5352` n `762`
- 24h: commodity avg `-0.5017` n `12`; crypto_alt avg `-0.2147` n `228`; crypto_major avg `-0.4463` n `8`; equity avg `-0.0126` n `88`; fx avg `0.0152` n `6`; index avg `-0.0178` n `23`; metal avg `-0.299` n `20`; unknown avg `15.543` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1831`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
