# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T04:56:28.824466+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `-0.2404` n `228`; crypto_major avg `-0.2628` n `8`; equity avg `-0.0609` n `88`; fx avg `-0.0021` n `6`; index avg `-0.0083` n `23`; metal avg `-0.0601` n `20`; unknown avg `0.7694` n `764`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.6348` n `228`; crypto_major avg `-0.6994` n `8`; equity avg `-0.2598` n `88`; fx avg `0.0011` n `6`; index avg `-0.0675` n `23`; metal avg `-0.2775` n `20`; unknown avg `7.7552` n `764`
- 4h: commodity avg `0.0086` n `12`; crypto_alt avg `0.6441` n `228`; crypto_major avg `0.3605` n `8`; equity avg `0.1872` n `88`; fx avg `0.0617` n `6`; index avg `0.0124` n `23`; metal avg `-0.1061` n `20`; unknown avg `-0.5981` n `764`
- 24h: commodity avg `-0.2726` n `12`; crypto_alt avg `-0.3981` n `228`; crypto_major avg `-0.4415` n `8`; equity avg `-0.1212` n `88`; fx avg `0.0426` n `6`; index avg `-0.1063` n `23`; metal avg `-0.3506` n `20`; unknown avg `-1.0642` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
