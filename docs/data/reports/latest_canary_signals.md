# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T03:52:30.824508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `0.1182` n `230`; crypto_major avg `0.1077` n `8`; equity avg `0.2334` n `102`; fx avg `-0.002` n `6`; index avg `0.0873` n `25`; metal avg `0.0612` n `20`; unknown avg `0.2861` n `779`
- 1h: commodity avg `0.0545` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `-0.1385` n `8`; equity avg `-0.3189` n `102`; fx avg `-0.0173` n `6`; index avg `-0.0211` n `25`; metal avg `-0.1104` n `20`; unknown avg `0.1738` n `779`
- 4h: commodity avg `-0.067` n `12`; crypto_alt avg `0.6156` n `230`; crypto_major avg `0.2475` n `8`; equity avg `0.1298` n `102`; fx avg `-0.0339` n `6`; index avg `0.1009` n `25`; metal avg `-0.2617` n `20`; unknown avg `0.2064` n `778`
- 24h: commodity avg `0.4368` n `12`; crypto_alt avg `0.2774` n `230`; crypto_major avg `0.5208` n `8`; equity avg `-1.2815` n `102`; fx avg `0.017` n `6`; index avg `0.024` n `25`; metal avg `0.1884` n `20`; unknown avg `-0.4776` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
