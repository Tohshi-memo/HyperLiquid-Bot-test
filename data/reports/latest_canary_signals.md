# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T14:07:39.849493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `-0.299` n `228`; crypto_major avg `-0.3805` n `8`; equity avg `0.1052` n `79`; fx avg `-0.0064` n `6`; index avg `0.0501` n `23`; metal avg `-0.0396` n `20`; unknown avg `0.15` n `722`
- 1h: commodity avg `-0.2958` n `12`; crypto_alt avg `0.1232` n `228`; crypto_major avg `0.2446` n `8`; equity avg `0.6535` n `79`; fx avg `-0.0233` n `6`; index avg `0.0859` n `23`; metal avg `0.1409` n `20`; unknown avg `0.2925` n `722`
- 4h: commodity avg `-0.4524` n `12`; crypto_alt avg `1.0501` n `228`; crypto_major avg `1.0283` n `8`; equity avg `0.9237` n `79`; fx avg `-0.0086` n `6`; index avg `0.1595` n `23`; metal avg `-0.0211` n `18`; unknown avg `1.244` n `701`
- 24h: commodity avg `-0.7081` n `12`; crypto_alt avg `0.8335` n `228`; crypto_major avg `1.3559` n `8`; equity avg `0.9308` n `79`; fx avg `-0.0048` n `6`; index avg `0.2341` n `23`; metal avg `0.5631` n `18`; unknown avg `0.9422` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
