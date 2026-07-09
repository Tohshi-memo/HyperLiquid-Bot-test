# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T16:37:07.767099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `0.1135` n `229`; crypto_major avg `0.1587` n `8`; equity avg `-0.1337` n `91`; fx avg `0.0006` n `6`; index avg `-0.0221` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.0692` n `765`
- 1h: commodity avg `-0.1298` n `12`; crypto_alt avg `-0.088` n `229`; crypto_major avg `-0.0261` n `8`; equity avg `-0.1575` n `91`; fx avg `-0.0008` n `6`; index avg `-0.0033` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0941` n `765`
- 4h: commodity avg `-0.8356` n `12`; crypto_alt avg `-0.3013` n `229`; crypto_major avg `-0.1069` n `8`; equity avg `0.408` n `91`; fx avg `-0.0366` n `6`; index avg `0.1006` n `25`; metal avg `0.2521` n `20`; unknown avg `-0.0139` n `765`
- 24h: commodity avg `-1.2565` n `12`; crypto_alt avg `1.346` n `229`; crypto_major avg `0.8581` n `8`; equity avg `2.9413` n `91`; fx avg `0.033` n `6`; index avg `0.4656` n `25`; metal avg `1.3438` n `20`; unknown avg `1.2259` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
