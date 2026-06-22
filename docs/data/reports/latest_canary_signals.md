# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T01:37:33.055481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `0.3432` n `228`; crypto_major avg `0.3067` n `8`; equity avg `0.0524` n `78`; fx avg `0.0135` n `6`; index avg `0.0124` n `23`; metal avg `-0.1486` n `18`; unknown avg `1.4211` n `702`
- 1h: commodity avg `-0.3047` n `12`; crypto_alt avg `0.7278` n `228`; crypto_major avg `0.6532` n `8`; equity avg `0.3339` n `78`; fx avg `0.0856` n `6`; index avg `0.1291` n `23`; metal avg `0.3325` n `18`; unknown avg `0.5212` n `694`
- 4h: commodity avg `-0.5601` n `12`; crypto_alt avg `0.8775` n `228`; crypto_major avg `0.7568` n `8`; equity avg `-0.4406` n `78`; fx avg `0.158` n `6`; index avg `0.0771` n `23`; metal avg `0.5626` n `18`; unknown avg `0.8612` n `694`
- 24h: commodity avg `-0.252` n `12`; crypto_alt avg `0.4473` n `228`; crypto_major avg `-0.1779` n `8`; equity avg `-0.3838` n `78`; fx avg `-0.0067` n `6`; index avg `0.0708` n `23`; metal avg `0.4423` n `18`; unknown avg `1.1563` n `638`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
