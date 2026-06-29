# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T03:52:28.868752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0573` n `228`; crypto_major avg `0.0537` n `8`; equity avg `0.2211` n `88`; fx avg `-0.0015` n `6`; index avg `0.0765` n `23`; metal avg `0.0321` n `20`; unknown avg `-0.279` n `764`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `0.4955` n `228`; crypto_major avg `0.3429` n `8`; equity avg `0.2397` n `88`; fx avg `0.0018` n `6`; index avg `0.0178` n `23`; metal avg `0.0314` n `20`; unknown avg `-0.0873` n `764`
- 4h: commodity avg `0.1025` n `12`; crypto_alt avg `1.117` n `228`; crypto_major avg `0.7055` n `8`; equity avg `-0.3242` n `88`; fx avg `0.1014` n `6`; index avg `-0.1585` n `23`; metal avg `0.0961` n `20`; unknown avg `0.2043` n `764`
- 24h: commodity avg `-0.2553` n `12`; crypto_alt avg `0.4923` n `228`; crypto_major avg `0.2488` n `8`; equity avg `0.1281` n `88`; fx avg `0.0497` n `6`; index avg `-0.028` n `23`; metal avg `-0.0904` n `20`; unknown avg `-0.7781` n `722`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
