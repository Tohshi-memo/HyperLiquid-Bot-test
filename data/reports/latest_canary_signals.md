# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T07:07:25.338918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0401` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `-0.0107` n `8`; equity avg `0.1966` n `120`; fx avg `-0.0058` n `6`; index avg `0.0119` n `25`; metal avg `-0.0158` n `20`; unknown avg `-0.0` n `789`
- 1h: commodity avg `0.0075` n `12`; crypto_alt avg `0.2709` n `230`; crypto_major avg `0.2287` n `8`; equity avg `0.8612` n `120`; fx avg `0.0298` n `6`; index avg `0.1706` n `25`; metal avg `0.089` n `20`; unknown avg `0.0603` n `789`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `0.2888` n `230`; crypto_major avg `0.1896` n `8`; equity avg `0.0601` n `120`; fx avg `-0.0059` n `6`; index avg `0.0692` n `25`; metal avg `-0.0431` n `20`; unknown avg `-0.0898` n `757`
- 24h: commodity avg `0.3561` n `12`; crypto_alt avg `0.3373` n `230`; crypto_major avg `-0.0501` n `8`; equity avg `-2.9629` n `120`; fx avg `-0.1437` n `6`; index avg `-0.3925` n `25`; metal avg `-0.6529` n `20`; unknown avg `-0.2662` n `756`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
