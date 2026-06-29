# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T04:07:27.587036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `-0.1515` n `228`; crypto_major avg `-0.0893` n `8`; equity avg `-0.0473` n `88`; fx avg `0.0087` n `6`; index avg `0.0058` n `23`; metal avg `-0.0616` n `20`; unknown avg `37.0238` n `764`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.0646` n `228`; crypto_major avg `-0.2075` n `8`; equity avg `-0.0207` n `88`; fx avg `0.0131` n `6`; index avg `0.0115` n `23`; metal avg `-0.0322` n `20`; unknown avg `8.2702` n `764`
- 4h: commodity avg `0.1271` n `12`; crypto_alt avg `1.278` n `228`; crypto_major avg `1.1517` n `8`; equity avg `-0.0765` n `88`; fx avg `0.0927` n `6`; index avg `-0.0304` n `23`; metal avg `0.1247` n `20`; unknown avg `0.0425` n `764`
- 24h: commodity avg `-0.2382` n `12`; crypto_alt avg `0.1941` n `228`; crypto_major avg `0.1321` n `8`; equity avg `0.0678` n `88`; fx avg `0.057` n `6`; index avg `-0.0242` n `23`; metal avg `-0.1523` n `20`; unknown avg `-0.7733` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
