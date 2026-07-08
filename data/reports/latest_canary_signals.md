# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T22:52:32.494618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.0509` n `229`; crypto_major avg `-0.0035` n `8`; equity avg `0.0119` n `91`; fx avg `-0.0112` n `6`; index avg `0.0014` n `25`; metal avg `0.0214` n `20`; unknown avg `-0.0318` n `764`
- 1h: commodity avg `-0.0404` n `12`; crypto_alt avg `0.2624` n `229`; crypto_major avg `0.1094` n `8`; equity avg `0.0687` n `91`; fx avg `-0.0091` n `6`; index avg `0.0412` n `25`; metal avg `0.0744` n `20`; unknown avg `-0.057` n `764`
- 4h: commodity avg `0.1872` n `12`; crypto_alt avg `0.0328` n `229`; crypto_major avg `0.1083` n `8`; equity avg `0.5672` n `91`; fx avg `-0.0024` n `6`; index avg `0.0503` n `25`; metal avg `-0.0854` n `20`; unknown avg `1.0643` n `764`
- 24h: commodity avg `0.3505` n `12`; crypto_alt avg `-1.6151` n `229`; crypto_major avg `-2.3963` n `8`; equity avg `1.4665` n `91`; fx avg `0.0055` n `6`; index avg `0.0296` n `25`; metal avg `-0.6444` n `20`; unknown avg `-0.0377` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
