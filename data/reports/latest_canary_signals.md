# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T00:37:28.711629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `12`; crypto_alt avg `0.0747` n `228`; crypto_major avg `0.0557` n `8`; equity avg `0.2063` n `86`; fx avg `0.0021` n `6`; index avg `0.0456` n `23`; metal avg `-0.0277` n `20`; unknown avg `-0.0443` n `764`
- 1h: commodity avg `0.0277` n `12`; crypto_alt avg `0.5739` n `228`; crypto_major avg `0.5316` n `8`; equity avg `0.8412` n `86`; fx avg `0.05` n `6`; index avg `0.2004` n `23`; metal avg `0.2065` n `20`; unknown avg `0.1513` n `764`
- 4h: commodity avg `-0.0978` n `12`; crypto_alt avg `0.2804` n `228`; crypto_major avg `0.5576` n `8`; equity avg `0.5418` n `86`; fx avg `0.0282` n `6`; index avg `0.229` n `23`; metal avg `-0.0876` n `20`; unknown avg `0.1637` n `756`
- 24h: commodity avg `-0.452` n `12`; crypto_alt avg `-1.6016` n `228`; crypto_major avg `-2.4901` n `8`; equity avg `-1.8571` n `86`; fx avg `-0.1759` n `6`; index avg `-0.506` n `23`; metal avg `-1.1719` n `20`; unknown avg `0.698` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
