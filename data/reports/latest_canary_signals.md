# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T03:22:25.350579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.058` n `229`; crypto_major avg `0.1228` n `8`; equity avg `-0.0359` n `91`; fx avg `-0.0002` n `6`; index avg `0.0044` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0397` n `764`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `-0.4485` n `229`; crypto_major avg `-0.3788` n `8`; equity avg `-0.8154` n `91`; fx avg `0.0125` n `6`; index avg `-0.2101` n `25`; metal avg `-0.2918` n `20`; unknown avg `-0.246` n `764`
- 4h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.1435` n `229`; crypto_major avg `-0.3054` n `8`; equity avg `-0.2014` n `91`; fx avg `0.0285` n `6`; index avg `-0.1582` n `25`; metal avg `-0.1733` n `20`; unknown avg `-0.2673` n `764`
- 24h: commodity avg `0.3329` n `12`; crypto_alt avg `-0.906` n `229`; crypto_major avg `-1.4927` n `8`; equity avg `0.0294` n `91`; fx avg `0.0518` n `6`; index avg `-0.3055` n `25`; metal avg `-1.1513` n `20`; unknown avg `0.0323` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
