# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T21:07:27.695605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.0096` n `228`; crypto_major avg `0.0071` n `8`; equity avg `-0.005` n `78`; fx avg `-0.0384` n `6`; index avg `-0.0075` n `23`; metal avg `0.0087` n `18`; unknown avg `-0.42` n `687`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.1178` n `228`; crypto_major avg `0.0416` n `8`; equity avg `0.0223` n `78`; fx avg `-0.0395` n `6`; index avg `-0.0202` n `23`; metal avg `0.0633` n `18`; unknown avg `-0.3837` n `687`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `0.0359` n `228`; crypto_major avg `0.4308` n `8`; equity avg `0.0306` n `78`; fx avg `-0.036` n `6`; index avg `-0.0173` n `23`; metal avg `0.182` n `18`; unknown avg `-0.3235` n `687`
- 24h: commodity avg `0.2993` n `12`; crypto_alt avg `-3.6286` n `228`; crypto_major avg `-4.494` n `8`; equity avg `0.7034` n `78`; fx avg `-0.1326` n `6`; index avg `0.2056` n `23`; metal avg `-4.1013` n `18`; unknown avg `-0.5716` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
