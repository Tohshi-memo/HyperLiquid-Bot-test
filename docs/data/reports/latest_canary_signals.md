# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T04:07:27.434996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.142` n `228`; crypto_major avg `0.0271` n `8`; equity avg `0.0123` n `88`; fx avg `0.0015` n `6`; index avg `0.0016` n `23`; metal avg `0.0005` n `20`; unknown avg `-0.2726` n `764`
- 1h: commodity avg `-0.1606` n `12`; crypto_alt avg `0.2927` n `228`; crypto_major avg `0.0806` n `8`; equity avg `0.0238` n `88`; fx avg `-0.0004` n `6`; index avg `0.0305` n `23`; metal avg `0.0155` n `20`; unknown avg `-0.2094` n `764`
- 4h: commodity avg `-0.0747` n `12`; crypto_alt avg `0.4869` n `228`; crypto_major avg `0.1049` n `8`; equity avg `-0.0122` n `88`; fx avg `-0.0224` n `6`; index avg `-0.0422` n `23`; metal avg `0.0254` n `20`; unknown avg `15.0938` n `722`
- 24h: commodity avg `0.1814` n `12`; crypto_alt avg `-0.6034` n `228`; crypto_major avg `-1.4573` n `8`; equity avg `0.0687` n `88`; fx avg `-0.0154` n `6`; index avg `-0.1233` n `23`; metal avg `-0.0363` n `20`; unknown avg `9.2008` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2193`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
