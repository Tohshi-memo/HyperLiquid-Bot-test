# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T08:07:31.375118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.0467` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.0195` n `102`; fx avg `0.0019` n `6`; index avg `-0.0073` n `25`; metal avg `0.0916` n `20`; unknown avg `0.0106` n `779`
- 1h: commodity avg `-0.0964` n `12`; crypto_alt avg `-0.2312` n `230`; crypto_major avg `-0.1435` n `8`; equity avg `-0.249` n `102`; fx avg `0.0317` n `6`; index avg `-0.0826` n `25`; metal avg `0.058` n `20`; unknown avg `8.4565` n `779`
- 4h: commodity avg `0.1368` n `12`; crypto_alt avg `-0.1597` n `230`; crypto_major avg `-0.1483` n `8`; equity avg `-0.2915` n `102`; fx avg `-0.0402` n `6`; index avg `-0.1417` n `25`; metal avg `0.0063` n `20`; unknown avg `1.3976` n `747`
- 24h: commodity avg `0.7375` n `12`; crypto_alt avg `-0.6451` n `230`; crypto_major avg `-0.8771` n `8`; equity avg `-3.2611` n `102`; fx avg `-0.0083` n `6`; index avg `-0.5252` n `25`; metal avg `-0.0122` n `20`; unknown avg `-0.5495` n `745`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
