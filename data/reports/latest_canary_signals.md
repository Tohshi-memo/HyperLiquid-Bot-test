# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T10:22:27.178749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.0227` n `228`; crypto_major avg `-0.0328` n `8`; equity avg `0.0083` n `88`; fx avg `-0.0056` n `6`; index avg `-0.003` n `23`; metal avg `0.0036` n `20`; unknown avg `-0.1697` n `764`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.3259` n `228`; crypto_major avg `-0.3457` n `8`; equity avg `-0.071` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0128` n `23`; metal avg `0.0018` n `20`; unknown avg `1.8905` n `750`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `0.5487` n `228`; crypto_major avg `0.6105` n `8`; equity avg `0.2417` n `88`; fx avg `0.0188` n `6`; index avg `0.0668` n `23`; metal avg `0.0088` n `20`; unknown avg `-0.3399` n `742`
- 24h: commodity avg `0.1403` n `12`; crypto_alt avg `-0.1448` n `228`; crypto_major avg `-0.895` n `8`; equity avg `0.068` n `88`; fx avg `-0.0058` n `6`; index avg `-0.0744` n `23`; metal avg `-0.0142` n `20`; unknown avg `16.2394` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
