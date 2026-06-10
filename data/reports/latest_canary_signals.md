# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T04:22:22.735123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0519` n `12`; crypto_alt avg `0.0839` n `228`; crypto_major avg `-0.0387` n `8`; equity avg `-0.1176` n `74`; fx avg `-0.0069` n `6`; index avg `-0.1793` n `23`; metal avg `-0.1114` n `18`; unknown avg `-0.0169` n `547`
- 1h: commodity avg `-0.1249` n `12`; crypto_alt avg `-0.0499` n `228`; crypto_major avg `-0.1285` n `8`; equity avg `-0.474` n `74`; fx avg `0.0045` n `6`; index avg `-0.2338` n `23`; metal avg `0.0255` n `18`; unknown avg `-0.4776` n `547`
- 4h: commodity avg `-0.3832` n `12`; crypto_alt avg `-0.701` n `228`; crypto_major avg `-1.0541` n `8`; equity avg `-1.163` n `74`; fx avg `0.1253` n `6`; index avg `-0.5332` n `23`; metal avg `-1.1933` n `18`; unknown avg `-0.7758` n `547`
- 24h: commodity avg `-0.5575` n `12`; crypto_alt avg `-0.3643` n `228`; crypto_major avg `-2.7622` n `8`; equity avg `-3.5417` n `74`; fx avg `0.1651` n `6`; index avg `-1.6674` n `23`; metal avg `-2.9539` n `18`; unknown avg `0.8079` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0412`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0408`, n `668`, weak_sample_signal
