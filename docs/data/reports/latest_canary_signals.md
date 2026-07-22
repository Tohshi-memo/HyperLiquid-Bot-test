# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T17:52:25.852553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.0443` n `230`; crypto_major avg `0.103` n `8`; equity avg `-0.1864` n `98`; fx avg `0.0046` n `6`; index avg `-0.0214` n `25`; metal avg `0.0215` n `20`; unknown avg `-0.0128` n `773`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `-0.2138` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `-0.2647` n `98`; fx avg `0.0155` n `6`; index avg `-0.0149` n `25`; metal avg `-0.0321` n `20`; unknown avg `0.0501` n `773`
- 4h: commodity avg `0.0832` n `12`; crypto_alt avg `0.1052` n `230`; crypto_major avg `0.3783` n `8`; equity avg `-0.1389` n `98`; fx avg `-0.0209` n `6`; index avg `0.0917` n `25`; metal avg `-0.1462` n `20`; unknown avg `-0.0593` n `773`
- 24h: commodity avg `0.6449` n `12`; crypto_alt avg `0.1887` n `230`; crypto_major avg `-0.2209` n `8`; equity avg `-0.5414` n `98`; fx avg `-0.0411` n `6`; index avg `-0.1037` n `25`; metal avg `0.3773` n `20`; unknown avg `0.9441` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0809`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0777`, n `666`, weak_sample_signal
