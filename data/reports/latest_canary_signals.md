# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T12:52:30.722177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0739` n `228`; crypto_major avg `0.0076` n `8`; equity avg `0.0192` n `88`; fx avg `0.0` n `6`; index avg `0.0031` n `23`; metal avg `-0.0041` n `20`; unknown avg `0.0491` n `764`
- 1h: commodity avg `-0.0376` n `12`; crypto_alt avg `-0.006` n `228`; crypto_major avg `0.0037` n `8`; equity avg `0.0152` n `88`; fx avg `0.0034` n `6`; index avg `-0.0041` n `23`; metal avg `0.0092` n `20`; unknown avg `0.0342` n `764`
- 4h: commodity avg `0.0302` n `12`; crypto_alt avg `-0.1413` n `228`; crypto_major avg `-0.2044` n `8`; equity avg `-0.0127` n `88`; fx avg `0.0255` n `6`; index avg `-0.0016` n `23`; metal avg `-0.0015` n `20`; unknown avg `-1.1019` n `750`
- 24h: commodity avg `0.1179` n `12`; crypto_alt avg `-0.108` n `228`; crypto_major avg `-0.6412` n `8`; equity avg `0.1141` n `88`; fx avg `0.0014` n `6`; index avg `-0.0469` n `23`; metal avg `-0.0143` n `20`; unknown avg `15.5809` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
