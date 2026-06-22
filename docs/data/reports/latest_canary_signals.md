# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T14:22:37.501506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `-0.1345` n `228`; crypto_major avg `-0.2201` n `8`; equity avg `-0.6771` n `79`; fx avg `-0.0074` n `6`; index avg `-0.041` n `23`; metal avg `-0.1812` n `20`; unknown avg `0.0201` n `722`
- 1h: commodity avg `-0.1049` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `-0.1215` n `8`; equity avg `-0.1647` n `79`; fx avg `-0.0299` n `6`; index avg `0.0193` n `23`; metal avg `-0.1175` n `20`; unknown avg `0.2239` n `722`
- 4h: commodity avg `-0.462` n `12`; crypto_alt avg `1.0279` n `228`; crypto_major avg `0.9505` n `8`; equity avg `0.1999` n `79`; fx avg `-0.0278` n `6`; index avg `0.1139` n `23`; metal avg `-0.2044` n `18`; unknown avg `1.2035` n `701`
- 24h: commodity avg `-0.7132` n `12`; crypto_alt avg `0.8137` n `228`; crypto_major avg `1.23` n `8`; equity avg `0.2317` n `79`; fx avg `-0.0191` n `6`; index avg `0.1926` n `23`; metal avg `0.3728` n `18`; unknown avg `0.9366` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
