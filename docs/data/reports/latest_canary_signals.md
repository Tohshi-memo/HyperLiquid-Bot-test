# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T20:22:28.923013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.0107` n `229`; crypto_major avg `-0.0008` n `8`; equity avg `-0.0057` n `91`; fx avg `0.0091` n `6`; index avg `-0.0029` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0189` n `765`
- 1h: commodity avg `0.0484` n `12`; crypto_alt avg `-0.0496` n `229`; crypto_major avg `0.0998` n `8`; equity avg `-0.2091` n `91`; fx avg `-0.0017` n `6`; index avg `0.0026` n `25`; metal avg `-0.0158` n `20`; unknown avg `-0.0868` n `765`
- 4h: commodity avg `-0.0797` n `12`; crypto_alt avg `0.4345` n `229`; crypto_major avg `0.4303` n `8`; equity avg `-0.218` n `91`; fx avg `-0.0261` n `6`; index avg `0.0414` n `25`; metal avg `-0.355` n `20`; unknown avg `-0.0294` n `765`
- 24h: commodity avg `-1.1941` n `12`; crypto_alt avg `1.1681` n `229`; crypto_major avg `0.5826` n `8`; equity avg `1.7611` n `91`; fx avg `0.0274` n `6`; index avg `0.3889` n `25`; metal avg `0.6334` n `20`; unknown avg `-0.0135` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
