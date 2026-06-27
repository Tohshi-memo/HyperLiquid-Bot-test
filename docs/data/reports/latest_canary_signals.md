# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T01:22:27.051225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.0269` n `228`; crypto_major avg `0.0858` n `8`; equity avg `0.0901` n `88`; fx avg `-0.0122` n `6`; index avg `0.0041` n `23`; metal avg `0.0086` n `20`; unknown avg `0.1642` n `764`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0128` n `228`; crypto_major avg `-0.1379` n `8`; equity avg `-0.0083` n `88`; fx avg `-0.0005` n `6`; index avg `0.0099` n `23`; metal avg `-0.001` n `20`; unknown avg `0.4304` n `764`
- 4h: commodity avg `0.0104` n `12`; crypto_alt avg `0.2025` n `228`; crypto_major avg `0.0939` n `8`; equity avg `0.272` n `88`; fx avg `-0.0295` n `6`; index avg `0.0421` n `23`; metal avg `0.0797` n `20`; unknown avg `-0.0988` n `748`
- 24h: commodity avg `-0.2204` n `12`; crypto_alt avg `1.6734` n `228`; crypto_major avg `1.5081` n `8`; equity avg `0.2316` n `87`; fx avg `-0.0469` n `6`; index avg `-0.2344` n `23`; metal avg `0.8051` n `20`; unknown avg `0.2334` n `700`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2126`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
