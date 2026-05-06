# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T20:07:26.706290+00:00`
- Correlation status: `ready`
- Asset price records: `484`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1151` n `12`; crypto_alt avg `0.3547` n `228`; crypto_major avg `0.1747` n `8`; equity avg `0.1432` n `65`; fx avg `0.0168` n `4`; index avg `0.0928` n `23`; metal avg `0.029` n `18`; unknown avg `0.1002` n `356`
- 1h: commodity avg `0.1232` n `12`; crypto_alt avg `0.1854` n `228`; crypto_major avg `0.2204` n `8`; equity avg `0.4872` n `65`; fx avg `0.0181` n `4`; index avg `0.2264` n `23`; metal avg `0.164` n `18`; unknown avg `0.0737` n `356`
- 4h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0315` n `228`; crypto_major avg `-0.0778` n `8`; equity avg `0.7663` n `65`; fx avg `-0.0497` n `4`; index avg `0.508` n `23`; metal avg `0.2755` n `18`; unknown avg `-0.3432` n `356`
- 24h: commodity avg `-2.4508` n `7`; crypto_alt avg `2.5891` n `223`; crypto_major avg `0.6289` n `7`; equity avg `3.0851` n `47`; fx avg `-0.482` n `4`; index avg `2.1077` n `6`; metal avg `3.5667` n `7`; unknown avg `3.3808` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1769`, n `476`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1641`, n `476`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1552`, n `476`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.145`, n `476`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `480`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `480`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `476`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `480`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `476`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0721`, n `480`, weak_sample_signal
