# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T20:07:27.299911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.1273` n `230`; crypto_major avg `0.1381` n `8`; equity avg `0.1747` n `121`; fx avg `-0.0145` n `6`; index avg `-0.0133` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.0777` n `792`
- 1h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0567` n `230`; crypto_major avg `0.1463` n `8`; equity avg `0.3768` n `121`; fx avg `-0.0187` n `6`; index avg `0.0011` n `25`; metal avg `0.0832` n `20`; unknown avg `-0.2098` n `792`
- 4h: commodity avg `0.0586` n `12`; crypto_alt avg `-0.157` n `230`; crypto_major avg `-0.3566` n `8`; equity avg `0.4119` n `121`; fx avg `0.007` n `6`; index avg `-0.0301` n `25`; metal avg `0.0436` n `20`; unknown avg `1.0257` n `792`
- 24h: commodity avg `0.4239` n `12`; crypto_alt avg `4.9608` n `230`; crypto_major avg `7.1491` n `8`; equity avg `-0.479` n `121`; fx avg `0.1871` n `6`; index avg `-0.0295` n `25`; metal avg `0.2266` n `20`; unknown avg `2.9549` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
