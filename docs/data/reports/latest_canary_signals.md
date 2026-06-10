# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T11:07:29.236998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.6156` n `12`; crypto_alt avg `-0.7548` n `228`; crypto_major avg `-0.4322` n `8`; equity avg `-0.3653` n `74`; fx avg `-0.0129` n `6`; index avg `-0.1024` n `23`; metal avg `-0.3181` n `18`; unknown avg `-0.0357` n `547`
- 1h: commodity avg `0.6516` n `12`; crypto_alt avg `-0.5266` n `228`; crypto_major avg `-0.0946` n `8`; equity avg `-0.1825` n `74`; fx avg `-0.0331` n `6`; index avg `-0.1741` n `23`; metal avg `0.0758` n `18`; unknown avg `0.0742` n `547`
- 4h: commodity avg `0.4987` n `12`; crypto_alt avg `-1.0435` n `228`; crypto_major avg `-0.5971` n `8`; equity avg `-0.9862` n `74`; fx avg `-0.048` n `6`; index avg `-0.5765` n `23`; metal avg `-0.6194` n `18`; unknown avg `0.247` n `547`
- 24h: commodity avg `0.2924` n `12`; crypto_alt avg `-1.9494` n `228`; crypto_major avg `-3.7565` n `8`; equity avg `-4.6082` n `74`; fx avg `-0.0541` n `6`; index avg `-2.563` n `23`; metal avg `-3.5911` n `18`; unknown avg `-0.0708` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
