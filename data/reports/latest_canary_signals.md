# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T02:07:21.527823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `-0.1303` n `235`; crypto_major avg `-0.0331` n `8`; equity avg `-0.0078` n `150`; fx avg `0.0` n `6`; index avg `0.0032` n `26`; metal avg `-0.003` n `20`; unknown avg `0.331` n `1115`
- 1h: commodity avg `0.0081` n `13`; crypto_alt avg `0.5737` n `235`; crypto_major avg `0.1849` n `8`; equity avg `0.0149` n `150`; fx avg `0.002` n `6`; index avg `0.0018` n `26`; metal avg `-0.0013` n `20`; unknown avg `-0.1605` n `1115`
- 4h: commodity avg `-0.0888` n `13`; crypto_alt avg `0.046` n `235`; crypto_major avg `-0.0755` n `8`; equity avg `-0.0437` n `150`; fx avg `0.0033` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0057` n `20`; unknown avg `2.557` n `1101`
- 24h: commodity avg `0.1019` n `13`; crypto_alt avg `1.3004` n `235`; crypto_major avg `0.2589` n `8`; equity avg `0.0933` n `150`; fx avg `-0.0072` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.3514` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
