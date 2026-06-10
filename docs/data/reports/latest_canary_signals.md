# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T09:22:30.434027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0491` n `12`; crypto_alt avg `-0.5335` n `228`; crypto_major avg `-0.5108` n `8`; equity avg `-0.3075` n `74`; fx avg `-0.0066` n `6`; index avg `-0.1126` n `23`; metal avg `-0.1505` n `18`; unknown avg `-0.0069` n `547`
- 1h: commodity avg `-0.5811` n `12`; crypto_alt avg `-0.9236` n `228`; crypto_major avg `-0.8728` n `8`; equity avg `-0.6904` n `74`; fx avg `-0.0125` n `6`; index avg `-0.2838` n `23`; metal avg `-0.122` n `18`; unknown avg `-0.14` n `547`
- 4h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.2097` n `228`; crypto_major avg `-0.472` n `8`; equity avg `-0.4708` n `74`; fx avg `0.0139` n `6`; index avg `-0.2003` n `23`; metal avg `0.0879` n `18`; unknown avg `-0.3484` n `537`
- 24h: commodity avg `-0.5248` n `12`; crypto_alt avg `-2.2644` n `228`; crypto_major avg `-4.6207` n `8`; equity avg `-4.6917` n `74`; fx avg `0.0596` n `6`; index avg `-2.4952` n `23`; metal avg `-3.5306` n `18`; unknown avg `0.3878` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
