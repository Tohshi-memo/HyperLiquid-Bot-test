# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T12:22:32.033828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0362` n `12`; crypto_alt avg `-0.0609` n `228`; crypto_major avg `-0.1362` n `8`; equity avg `-0.0081` n `74`; fx avg `0.0012` n `6`; index avg `-0.0008` n `23`; metal avg `-0.1168` n `18`; unknown avg `-0.036` n `547`
- 1h: commodity avg `0.3003` n `12`; crypto_alt avg `-0.3429` n `228`; crypto_major avg `-0.3928` n `8`; equity avg `-0.4295` n `74`; fx avg `-0.0085` n `6`; index avg `-0.148` n `23`; metal avg `-0.686` n `18`; unknown avg `-0.195` n `547`
- 4h: commodity avg `0.7431` n `12`; crypto_alt avg `-1.1357` n `228`; crypto_major avg `-0.7354` n `8`; equity avg `-0.7995` n `74`; fx avg `-0.0442` n `6`; index avg `-0.4127` n `23`; metal avg `-0.5287` n `18`; unknown avg `-0.0415` n `547`
- 24h: commodity avg `0.4603` n `12`; crypto_alt avg `-2.5985` n `228`; crypto_major avg `-4.0363` n `8`; equity avg `-4.7765` n `74`; fx avg `-0.096` n `6`; index avg `-2.6219` n `23`; metal avg `-4.2666` n `18`; unknown avg `0.2465` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
