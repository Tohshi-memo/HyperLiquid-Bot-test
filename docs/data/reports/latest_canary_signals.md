# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T08:37:28.817077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0163` n `12`; crypto_alt avg `-0.3218` n `232`; crypto_major avg `-0.3013` n `8`; equity avg `-0.2898` n `130`; fx avg `0.0046` n `6`; index avg `-0.079` n `26`; metal avg `-0.2524` n `20`; unknown avg `0.1611` n `792`
- 1h: commodity avg `0.1193` n `12`; crypto_alt avg `-1.0102` n `232`; crypto_major avg `-0.6496` n `8`; equity avg `-1.0582` n `130`; fx avg `0.0098` n `6`; index avg `-0.2064` n `26`; metal avg `-0.4637` n `20`; unknown avg `-0.1465` n `790`
- 4h: commodity avg `0.1862` n `12`; crypto_alt avg `-0.953` n `232`; crypto_major avg `-0.9897` n `8`; equity avg `-1.0543` n `130`; fx avg `-0.0024` n `6`; index avg `-0.2002` n `26`; metal avg `-0.5256` n `20`; unknown avg `-0.0172` n `770`
- 24h: commodity avg `0.4783` n `12`; crypto_alt avg `0.505` n `232`; crypto_major avg `0.239` n `8`; equity avg `-0.5461` n `130`; fx avg `0.0868` n `6`; index avg `-0.2435` n `26`; metal avg `-0.7101` n `20`; unknown avg `0.1194` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0427`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0396`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
