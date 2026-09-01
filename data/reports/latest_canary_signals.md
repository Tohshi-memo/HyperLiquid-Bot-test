# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T07:37:23.773788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `-0.2229` n `232`; crypto_major avg `-0.3033` n `8`; equity avg `-0.0474` n `130`; fx avg `-0.0202` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0973` n `20`; unknown avg `0.1392` n `792`
- 1h: commodity avg `0.0992` n `12`; crypto_alt avg `-0.163` n `232`; crypto_major avg `-0.451` n `8`; equity avg `-0.043` n `130`; fx avg `0.0039` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0886` n `20`; unknown avg `0.1691` n `790`
- 4h: commodity avg `0.1105` n `12`; crypto_alt avg `0.0683` n `232`; crypto_major avg `-0.4814` n `8`; equity avg `0.17` n `130`; fx avg `0.0137` n `6`; index avg `0.0212` n `26`; metal avg `-0.0891` n `20`; unknown avg `0.0809` n `770`
- 24h: commodity avg `0.6113` n `12`; crypto_alt avg `1.3088` n `232`; crypto_major avg `0.8135` n `8`; equity avg `0.3993` n `130`; fx avg `0.0566` n `6`; index avg `-0.0354` n `26`; metal avg `-0.301` n `20`; unknown avg `0.2753` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
