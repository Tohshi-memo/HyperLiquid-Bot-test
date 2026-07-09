# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T09:12:31.905847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.11` n `229`; crypto_major avg `-0.0927` n `8`; equity avg `-0.0433` n `91`; fx avg `-0.0014` n `6`; index avg `-0.0098` n `25`; metal avg `0.0096` n `20`; unknown avg `0.0023` n `764`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-0.1078` n `229`; crypto_major avg `-0.1285` n `8`; equity avg `-0.2302` n `91`; fx avg `-0.0233` n `6`; index avg `-0.0507` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0633` n `764`
- 4h: commodity avg `-0.326` n `12`; crypto_alt avg `0.532` n `229`; crypto_major avg `0.4357` n `8`; equity avg `0.6349` n `91`; fx avg `0.1078` n `6`; index avg `0.0936` n `25`; metal avg `0.6398` n `20`; unknown avg `0.1083` n `748`
- 24h: commodity avg `-0.7026` n `12`; crypto_alt avg `1.8484` n `229`; crypto_major avg `1.0961` n `8`; equity avg `3.78` n `91`; fx avg `0.1158` n `6`; index avg `0.5993` n `25`; metal avg `0.654` n `20`; unknown avg `0.6215` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1008`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0708`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0682`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0671`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0643`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0589`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0587`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0574`, n `670`, weak_sample_signal
