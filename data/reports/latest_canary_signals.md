# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T23:07:29.849087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `12`; crypto_alt avg `0.1503` n `228`; crypto_major avg `0.1208` n `8`; equity avg `0.0131` n `88`; fx avg `0.0` n `6`; index avg `0.009` n `23`; metal avg `0.0075` n `20`; unknown avg `-0.4249` n `764`
- 1h: commodity avg `-0.0881` n `12`; crypto_alt avg `0.2441` n `228`; crypto_major avg `0.3003` n `8`; equity avg `0.0523` n `88`; fx avg `0.0144` n `6`; index avg `0.0029` n `23`; metal avg `0.0215` n `20`; unknown avg `-0.6447` n `764`
- 4h: commodity avg `0.0481` n `12`; crypto_alt avg `-0.6536` n `228`; crypto_major avg `-0.6093` n `8`; equity avg `-0.0366` n `88`; fx avg `0.0092` n `6`; index avg `-0.0362` n `23`; metal avg `-0.0118` n `20`; unknown avg `-0.6685` n `764`
- 24h: commodity avg `0.0734` n `12`; crypto_alt avg `-0.5153` n `228`; crypto_major avg `-0.7341` n `8`; equity avg `0.3641` n `88`; fx avg `0.0439` n `6`; index avg `-0.0284` n `23`; metal avg `-0.0344` n `20`; unknown avg `-1.021` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
