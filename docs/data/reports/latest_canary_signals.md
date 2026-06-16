# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T05:07:38.560653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0314` n `12`; crypto_alt avg `0.4566` n `228`; crypto_major avg `0.4433` n `8`; equity avg `0.1173` n `77`; fx avg `0.0061` n `6`; index avg `0.1957` n `23`; metal avg `0.1202` n `18`; unknown avg `-0.1082` n `687`
- 1h: commodity avg `-0.1438` n `12`; crypto_alt avg `-0.2729` n `228`; crypto_major avg `-0.0232` n `8`; equity avg `0.0461` n `77`; fx avg `-0.0316` n `6`; index avg `0.2022` n `23`; metal avg `0.0065` n `18`; unknown avg `0.0697` n `687`
- 4h: commodity avg `-0.341` n `12`; crypto_alt avg `-0.4565` n `228`; crypto_major avg `0.0355` n `8`; equity avg `0.5133` n `77`; fx avg `-0.0329` n `6`; index avg `0.2895` n `23`; metal avg `0.2864` n `18`; unknown avg `0.5218` n `671`
- 24h: commodity avg `0.2871` n `12`; crypto_alt avg `0.487` n `228`; crypto_major avg `2.3079` n `8`; equity avg `1.1684` n `76`; fx avg `-0.1083` n `6`; index avg `0.6869` n `23`; metal avg `-0.2547` n `18`; unknown avg `0.976` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
