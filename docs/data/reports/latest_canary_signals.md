# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T12:07:32.459514+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0131` n `12`; crypto_alt avg `0.1206` n `228`; crypto_major avg `0.0956` n `8`; equity avg `0.0558` n `86`; fx avg `-0.0193` n `6`; index avg `-0.0004` n `23`; metal avg `0.0343` n `20`; unknown avg `0.2592` n `764`
- 1h: commodity avg `-0.0759` n `12`; crypto_alt avg `0.4625` n `228`; crypto_major avg `0.365` n `8`; equity avg `0.3919` n `86`; fx avg `-0.0167` n `6`; index avg `0.0619` n `23`; metal avg `-0.0102` n `20`; unknown avg `0.3283` n `764`
- 4h: commodity avg `-0.0653` n `12`; crypto_alt avg `-0.3435` n `228`; crypto_major avg `-0.6513` n `8`; equity avg `0.4561` n `86`; fx avg `-0.0544` n `6`; index avg `0.0428` n `23`; metal avg `0.1578` n `20`; unknown avg `0.1224` n `764`
- 24h: commodity avg `-0.5313` n `12`; crypto_alt avg `-4.2578` n `228`; crypto_major avg `-4.3008` n `8`; equity avg `-4.0535` n `85`; fx avg `-0.1531` n `6`; index avg `-0.883` n `23`; metal avg `-1.361` n `20`; unknown avg `0.2147` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
