# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T08:07:32.298747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `0.0817` n `228`; crypto_major avg `0.0528` n `8`; equity avg `-0.0252` n `88`; fx avg `0.0032` n `6`; index avg `0.0111` n `23`; metal avg `0.0012` n `20`; unknown avg `-0.731` n `764`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `0.1603` n `228`; crypto_major avg `0.1864` n `8`; equity avg `0.1235` n `88`; fx avg `0.0137` n `6`; index avg `0.0379` n `23`; metal avg `-0.0013` n `20`; unknown avg `-0.8383` n `756`
- 4h: commodity avg `0.1078` n `12`; crypto_alt avg `-0.0203` n `228`; crypto_major avg `0.0003` n `8`; equity avg `0.0979` n `88`; fx avg `0.0195` n `6`; index avg `0.027` n `23`; metal avg `-0.0338` n `20`; unknown avg `-0.8854` n `724`
- 24h: commodity avg `0.2621` n `12`; crypto_alt avg `-0.3332` n `228`; crypto_major avg `-1.2914` n `8`; equity avg `-0.0353` n `88`; fx avg `0.002` n `6`; index avg `-0.1021` n `23`; metal avg `-0.0464` n `20`; unknown avg `15.4114` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2175`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
