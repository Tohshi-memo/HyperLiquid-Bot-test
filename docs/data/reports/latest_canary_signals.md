# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T21:21:09.208170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.0055` n `228`; crypto_major avg `0.0056` n `8`; equity avg `0.0022` n `86`; fx avg `0.0008` n `6`; index avg `0.0025` n `23`; metal avg `0.011` n `20`; unknown avg `0.0477` n `764`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.0949` n `228`; crypto_major avg `-0.059` n `8`; equity avg `0.0387` n `86`; fx avg `-0.0029` n `6`; index avg `0.0194` n `23`; metal avg `0.0632` n `20`; unknown avg `0.4081` n `764`
- 4h: commodity avg `0.0065` n `12`; crypto_alt avg `0.5145` n `228`; crypto_major avg `0.0348` n `8`; equity avg `-0.5951` n `86`; fx avg `0.0008` n `6`; index avg `-0.0768` n `23`; metal avg `-0.2068` n `20`; unknown avg `0.4226` n `756`
- 24h: commodity avg `-0.4289` n `12`; crypto_alt avg `-2.5208` n `228`; crypto_major avg `-3.5458` n `8`; equity avg `-3.2913` n `86`; fx avg `-0.1579` n `6`; index avg `-0.9114` n `23`; metal avg `-1.1782` n `20`; unknown avg `0.7786` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
