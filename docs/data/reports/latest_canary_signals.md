# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T08:22:26.256906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.1808` n `228`; crypto_major avg `0.0623` n `8`; equity avg `0.0211` n `78`; fx avg `-0.0071` n `6`; index avg `0.0156` n `23`; metal avg `-0.0251` n `18`; unknown avg `0.0346` n `687`
- 1h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.0471` n `228`; crypto_major avg `-0.1887` n `8`; equity avg `0.0277` n `78`; fx avg `0.0029` n `6`; index avg `0.0112` n `23`; metal avg `-0.0157` n `18`; unknown avg `-0.0211` n `687`
- 4h: commodity avg `0.0881` n `12`; crypto_alt avg `0.4765` n `228`; crypto_major avg `0.9144` n `8`; equity avg `0.2325` n `78`; fx avg `-0.008` n `6`; index avg `-0.0101` n `23`; metal avg `0.0314` n `18`; unknown avg `0.0632` n `639`
- 24h: commodity avg `0.5239` n `12`; crypto_alt avg `-3.1742` n `228`; crypto_major avg `-3.5076` n `8`; equity avg `1.3413` n `78`; fx avg `-0.0961` n `6`; index avg `0.2859` n `23`; metal avg `-4.0984` n `18`; unknown avg `0.0636` n `530`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
