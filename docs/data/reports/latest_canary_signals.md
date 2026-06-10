# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T13:37:27.210685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.26` n `12`; crypto_alt avg `1.0009` n `228`; crypto_major avg `1.0951` n `8`; equity avg `1.0282` n `74`; fx avg `0.0316` n `6`; index avg `0.4221` n `23`; metal avg `0.6942` n `18`; unknown avg `0.3251` n `547`
- 1h: commodity avg `-0.1941` n `12`; crypto_alt avg `0.7202` n `228`; crypto_major avg `0.7796` n `8`; equity avg `0.5371` n `74`; fx avg `0.057` n `6`; index avg `0.087` n `23`; metal avg `0.4042` n `18`; unknown avg `0.0055` n `547`
- 4h: commodity avg `0.858` n `12`; crypto_alt avg `1.6776` n `228`; crypto_major avg `1.7435` n `8`; equity avg `1.5022` n `74`; fx avg `0.0126` n `6`; index avg `0.4417` n `23`; metal avg `0.6621` n `18`; unknown avg `0.4564` n `547`
- 24h: commodity avg `0.8453` n `12`; crypto_alt avg `0.136` n `228`; crypto_major avg `-1.2091` n `8`; equity avg `-2.58` n `74`; fx avg `-0.037` n `6`; index avg `-1.7177` n `23`; metal avg `-2.8992` n `18`; unknown avg `1.3683` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
