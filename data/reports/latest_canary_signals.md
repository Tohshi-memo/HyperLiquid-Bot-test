# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T22:22:25.575584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0898` n `12`; crypto_alt avg `-0.5889` n `228`; crypto_major avg `-0.7462` n `8`; equity avg `-0.0695` n `88`; fx avg `-0.013` n `6`; index avg `-0.0239` n `23`; metal avg `-0.2328` n `20`; unknown avg `0.201` n `764`
- 1h: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.1624` n `228`; crypto_major avg `-0.2629` n `8`; equity avg `0.0524` n `88`; fx avg `-0.0153` n `6`; index avg `0.0313` n `23`; metal avg `-0.1886` n `20`; unknown avg `0.0016` n `764`
- 4h: commodity avg `-0.3218` n `12`; crypto_alt avg `-0.6513` n `228`; crypto_major avg `-0.607` n `8`; equity avg `0.1844` n `88`; fx avg `-0.0722` n `6`; index avg `0.0918` n `23`; metal avg `-0.1689` n `20`; unknown avg `0.7722` n `764`
- 24h: commodity avg `-0.1691` n `12`; crypto_alt avg `-0.4971` n `228`; crypto_major avg `-0.9385` n `8`; equity avg `0.3435` n `88`; fx avg `-0.1019` n `6`; index avg `0.1236` n `23`; metal avg `-0.1473` n `20`; unknown avg `15.2148` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
