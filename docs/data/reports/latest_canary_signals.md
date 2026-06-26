# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T21:07:26.271862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.2081` n `228`; crypto_major avg `-0.1905` n `8`; equity avg `-0.0351` n `88`; fx avg `0.0375` n `6`; index avg `0.0099` n `23`; metal avg `-0.0322` n `20`; unknown avg `-0.3247` n `764`
- 1h: commodity avg `0.1937` n `12`; crypto_alt avg `-0.7313` n `228`; crypto_major avg `-0.8749` n `8`; equity avg `-0.077` n `88`; fx avg `0.0418` n `6`; index avg `0.0111` n `23`; metal avg `0.103` n `20`; unknown avg `-0.8041` n `764`
- 4h: commodity avg `0.1391` n `12`; crypto_alt avg `-0.794` n `228`; crypto_major avg `-0.9747` n `8`; equity avg `-0.4869` n `87`; fx avg `0.0308` n `6`; index avg `-0.2092` n `23`; metal avg `-0.0837` n `20`; unknown avg `-0.6615` n `764`
- 24h: commodity avg `-0.2091` n `12`; crypto_alt avg `1.8897` n `228`; crypto_major avg `1.7622` n `8`; equity avg `-0.6624` n `87`; fx avg `-0.0333` n `6`; index avg `-0.392` n `23`; metal avg `0.6553` n `20`; unknown avg `-0.5542` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
