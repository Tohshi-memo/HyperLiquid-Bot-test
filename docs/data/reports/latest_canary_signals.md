# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T05:52:24.096218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `0.0364` n `228`; crypto_major avg `0.0595` n `8`; equity avg `0.1142` n `74`; fx avg `0.0094` n `6`; index avg `0.0097` n `23`; metal avg `0.2911` n `18`; unknown avg `-0.0733` n `547`
- 1h: commodity avg `-0.4301` n `12`; crypto_alt avg `-0.1172` n `228`; crypto_major avg `-0.1427` n `8`; equity avg `0.1451` n `74`; fx avg `0.0224` n `6`; index avg `-0.0282` n `23`; metal avg `0.6768` n `18`; unknown avg `-0.1489` n `547`
- 4h: commodity avg `-0.6579` n `12`; crypto_alt avg `-1.2562` n `228`; crypto_major avg `-1.3167` n `8`; equity avg `-0.9604` n `74`; fx avg `0.0674` n `6`; index avg `-0.5879` n `23`; metal avg `-0.1894` n `18`; unknown avg `-0.8483` n `547`
- 24h: commodity avg `-0.9281` n `12`; crypto_alt avg `-2.164` n `228`; crypto_major avg `-4.3115` n `8`; equity avg `-4.0286` n `74`; fx avg `0.223` n `6`; index avg `-2.0137` n `23`; metal avg `-3.0539` n `18`; unknown avg `0.3663` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
