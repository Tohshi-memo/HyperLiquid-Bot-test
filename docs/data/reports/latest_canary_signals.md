# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T04:22:31.631738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0148` n `12`; crypto_alt avg `0.0174` n `228`; crypto_major avg `-0.0109` n `8`; equity avg `0.0044` n `88`; fx avg `0.0047` n `6`; index avg `0.0026` n `23`; metal avg `0.0063` n `20`; unknown avg `-0.108` n `764`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `0.1994` n `228`; crypto_major avg `-0.072` n `8`; equity avg `0.0201` n `88`; fx avg `0.0041` n `6`; index avg `0.0058` n `23`; metal avg `0.0172` n `20`; unknown avg `-0.6366` n `764`
- 4h: commodity avg `-0.0809` n `12`; crypto_alt avg `0.3085` n `228`; crypto_major avg `-0.0203` n `8`; equity avg `-0.0377` n `88`; fx avg `-0.0152` n `6`; index avg `-0.0307` n `23`; metal avg `0.0249` n `20`; unknown avg `14.926` n `722`
- 24h: commodity avg `0.1893` n `12`; crypto_alt avg `-0.7263` n `228`; crypto_major avg `-1.4735` n `8`; equity avg `0.0272` n `88`; fx avg `-0.0093` n `6`; index avg `-0.123` n `23`; metal avg `-0.0314` n `20`; unknown avg `9.1792` n `674`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2204`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
