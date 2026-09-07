# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T11:22:27.674821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `0.1647` n `232`; crypto_major avg `0.1095` n `8`; equity avg `-0.024` n `134`; fx avg `0.0018` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0351` n `20`; unknown avg `0.4309` n `796`
- 1h: commodity avg `0.2506` n `12`; crypto_alt avg `0.305` n `232`; crypto_major avg `0.0701` n `8`; equity avg `-0.0899` n `134`; fx avg `0.0277` n `6`; index avg `-0.0488` n `26`; metal avg `-0.064` n `20`; unknown avg `0.4456` n `794`
- 4h: commodity avg `0.1674` n `12`; crypto_alt avg `0.4688` n `232`; crypto_major avg `-0.0019` n `8`; equity avg `-0.0835` n `134`; fx avg `-0.0475` n `6`; index avg `-0.0471` n `26`; metal avg `-0.027` n `20`; unknown avg `1.5296` n `784`
- 24h: commodity avg `0.1941` n `12`; crypto_alt avg `0.0747` n `232`; crypto_major avg `-0.7728` n `8`; equity avg `0.1878` n `134`; fx avg `-0.0988` n `6`; index avg `-0.0232` n `26`; metal avg `-0.1768` n `20`; unknown avg `229.1257` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
