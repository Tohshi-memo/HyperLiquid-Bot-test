# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T15:37:18.505556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0527` n `12`; crypto_alt avg `0.1106` n `228`; crypto_major avg `0.1114` n `8`; equity avg `-0.1059` n `67`; fx avg `-0.0021` n `6`; index avg `-0.0182` n `23`; metal avg `-0.011` n `18`; unknown avg `0.0295` n `396`
- 1h: commodity avg `-0.228` n `12`; crypto_alt avg `0.2842` n `228`; crypto_major avg `0.1897` n `8`; equity avg `0.0058` n `67`; fx avg `-0.0043` n `6`; index avg `-0.0831` n `23`; metal avg `0.0777` n `18`; unknown avg `0.0029` n `396`
- 4h: commodity avg `0.6394` n `12`; crypto_alt avg `-0.9751` n `228`; crypto_major avg `-0.8475` n `8`; equity avg `-0.3829` n `67`; fx avg `0.0125` n `6`; index avg `-0.379` n `23`; metal avg `-0.5327` n `18`; unknown avg `1.4449` n `396`
- 24h: commodity avg `-1.5052` n `12`; crypto_alt avg `0.7448` n `228`; crypto_major avg `2.4506` n `8`; equity avg `1.5936` n `67`; fx avg `0.0679` n `6`; index avg `0.4929` n `23`; metal avg `0.5853` n `18`; unknown avg `1.8997` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
