# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T15:46:51.652272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0454` n `12`; crypto_alt avg `-0.2519` n `228`; crypto_major avg `-0.3595` n `8`; equity avg `-0.4256` n `77`; fx avg `0.001` n `6`; index avg `-0.2248` n `23`; metal avg `-0.1585` n `18`; unknown avg `-0.0639` n `687`
- 1h: commodity avg `0.0468` n `12`; crypto_alt avg `0.0444` n `228`; crypto_major avg `-0.0053` n `8`; equity avg `-0.5678` n `77`; fx avg `0.0233` n `6`; index avg `-0.3445` n `23`; metal avg `-0.0924` n `18`; unknown avg `0.5339` n `687`
- 4h: commodity avg `-0.1477` n `12`; crypto_alt avg `-1.448` n `228`; crypto_major avg `-1.2902` n `8`; equity avg `-1.7081` n `77`; fx avg `0.0274` n `6`; index avg `-0.8831` n `23`; metal avg `-0.417` n `18`; unknown avg `0.7371` n `687`
- 24h: commodity avg `-0.395` n `12`; crypto_alt avg `-2.7639` n `228`; crypto_major avg `-1.584` n `8`; equity avg `1.8308` n `77`; fx avg `-0.0284` n `6`; index avg `-0.828` n `23`; metal avg `-0.4677` n `18`; unknown avg `0.3361` n `623`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
