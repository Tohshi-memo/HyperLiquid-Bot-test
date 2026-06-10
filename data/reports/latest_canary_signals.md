# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T04:37:20.707696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0239` n `12`; crypto_alt avg `-0.5515` n `228`; crypto_major avg `-0.3902` n `8`; equity avg `-0.4016` n `74`; fx avg `-0.0032` n `6`; index avg `-0.1809` n `23`; metal avg `-0.2232` n `18`; unknown avg `-0.194` n `547`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `-0.6706` n `228`; crypto_major avg `-0.6657` n `8`; equity avg `-0.754` n `74`; fx avg `0.015` n `6`; index avg `-0.3836` n `23`; metal avg `-0.2948` n `18`; unknown avg `-0.7744` n `547`
- 4h: commodity avg `-0.4986` n `12`; crypto_alt avg `-0.9633` n `228`; crypto_major avg `-1.09` n `8`; equity avg `-1.2894` n `74`; fx avg `0.0828` n `6`; index avg `-0.5402` n `23`; metal avg `-0.8454` n `18`; unknown avg `-0.9313` n `547`
- 24h: commodity avg `-0.5546` n `12`; crypto_alt avg `-1.7524` n `228`; crypto_major avg `-4.0384` n `8`; equity avg `-4.1304` n `74`; fx avg `0.137` n `6`; index avg `-1.9021` n `23`; metal avg `-3.1383` n `18`; unknown avg `0.3893` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0441`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
