# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T18:22:20.100474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0845` n `12`; crypto_alt avg `-0.1395` n `228`; crypto_major avg `-0.0313` n `8`; equity avg `-0.0518` n `66`; fx avg `0.0065` n `6`; index avg `0.0424` n `23`; metal avg `-0.2445` n `18`; unknown avg `1.0979` n `384`
- 1h: commodity avg `0.2679` n `12`; crypto_alt avg `-0.1849` n `228`; crypto_major avg `-0.1321` n `8`; equity avg `0.2051` n `66`; fx avg `0.0038` n `6`; index avg `0.0164` n `23`; metal avg `0.0026` n `18`; unknown avg `1.1499` n `384`
- 4h: commodity avg `-0.894` n `12`; crypto_alt avg `0.8763` n `228`; crypto_major avg `0.5443` n `8`; equity avg `0.6543` n `66`; fx avg `-0.0038` n `6`; index avg `0.2048` n `23`; metal avg `0.4373` n `18`; unknown avg `0.6826` n `384`
- 24h: commodity avg `-2.5184` n `12`; crypto_alt avg `2.4643` n `228`; crypto_major avg `1.7969` n `8`; equity avg `1.1184` n `66`; fx avg `-0.0419` n `6`; index avg `0.5064` n `23`; metal avg `1.3584` n `18`; unknown avg `2.036` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0423`, n `668`, weak_sample_signal
