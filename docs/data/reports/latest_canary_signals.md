# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T11:52:29.291670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.2528` n `228`; crypto_major avg `0.2662` n `8`; equity avg `0.0178` n `74`; fx avg `-0.0108` n `6`; index avg `0.0679` n `23`; metal avg `-0.0124` n `18`; unknown avg `-0.0416` n `547`
- 1h: commodity avg `1.0717` n `12`; crypto_alt avg `-0.7415` n `228`; crypto_major avg `-0.2829` n `8`; equity avg `-0.6084` n `74`; fx avg `-0.0232` n `6`; index avg `-0.1562` n `23`; metal avg `-0.2879` n `18`; unknown avg `0.0364` n `547`
- 4h: commodity avg `0.9725` n `12`; crypto_alt avg `-1.2328` n `228`; crypto_major avg `-0.8875` n `8`; equity avg `-1.1449` n `74`; fx avg `-0.0668` n `6`; index avg `-0.5484` n `23`; metal avg `-0.2842` n `18`; unknown avg `0.3087` n `547`
- 24h: commodity avg `0.5543` n `12`; crypto_alt avg `-2.0658` n `228`; crypto_major avg `-3.435` n `8`; equity avg `-4.8827` n `74`; fx avg `-0.0854` n `6`; index avg `-2.6161` n `23`; metal avg `-3.6944` n `18`; unknown avg `0.3097` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
