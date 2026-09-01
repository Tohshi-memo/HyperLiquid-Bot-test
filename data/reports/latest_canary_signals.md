# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T10:18:59.392459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.0069` n `232`; crypto_major avg `0.0459` n `8`; equity avg `-0.0086` n `130`; fx avg `0.0016` n `6`; index avg `0.011` n `26`; metal avg `0.0962` n `20`; unknown avg `0.1002` n `792`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `-0.0189` n `232`; crypto_major avg `-0.0757` n `8`; equity avg `0.0777` n `130`; fx avg `0.0053` n `6`; index avg `0.023` n `26`; metal avg `0.0582` n `20`; unknown avg `-0.1445` n `790`
- 4h: commodity avg `0.1394` n `12`; crypto_alt avg `-1.2761` n `232`; crypto_major avg `-1.0958` n `8`; equity avg `-1.44` n `130`; fx avg `0.0351` n `6`; index avg `-0.2885` n `26`; metal avg `-0.5127` n `20`; unknown avg `-0.1498` n `788`
- 24h: commodity avg `0.2373` n `12`; crypto_alt avg `0.4165` n `232`; crypto_major avg `0.0219` n `8`; equity avg `-0.5888` n `130`; fx avg `0.0798` n `6`; index avg `-0.2476` n `26`; metal avg `-0.6644` n `20`; unknown avg `0.0817` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.031`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0293`, n `668`, weak_sample_signal
