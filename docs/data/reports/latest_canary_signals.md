# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T23:22:15.654587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `-0.1268` n `228`; crypto_major avg `-0.0838` n `8`; equity avg `0.0097` n `65`; fx avg `0.0` n `5`; index avg `-0.0037` n `23`; metal avg `-0.013` n `18`; unknown avg `0.5251` n `376`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.2582` n `228`; crypto_major avg `-0.1595` n `8`; equity avg `-0.0098` n `65`; fx avg `0.0` n `5`; index avg `0.0158` n `23`; metal avg `0.0039` n `18`; unknown avg `0.3027` n `376`
- 4h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.154` n `228`; crypto_major avg `-0.1779` n `8`; equity avg `0.3438` n `65`; fx avg `-0.0006` n `5`; index avg `0.1022` n `23`; metal avg `0.1567` n `18`; unknown avg `-0.2057` n `376`
- 24h: commodity avg `0.4502` n `12`; crypto_alt avg `-0.0834` n `228`; crypto_major avg `0.2359` n `8`; equity avg `0.7282` n `65`; fx avg `-0.0253` n `5`; index avg `0.3655` n `23`; metal avg `0.3184` n `18`; unknown avg `0.4521` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
