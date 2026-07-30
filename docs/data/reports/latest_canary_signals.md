# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T09:37:29.855094+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `12`; crypto_alt avg `0.0246` n `230`; crypto_major avg `0.1227` n `8`; equity avg `0.0973` n `102`; fx avg `-0.0183` n `6`; index avg `0.0161` n `25`; metal avg `0.033` n `20`; unknown avg `-0.0076` n `779`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `0.0891` n `230`; crypto_major avg `0.2953` n `8`; equity avg `0.3052` n `102`; fx avg `-0.0003` n `6`; index avg `0.0428` n `25`; metal avg `0.0713` n `20`; unknown avg `-0.0056` n `771`
- 4h: commodity avg `-0.2415` n `12`; crypto_alt avg `0.2697` n `230`; crypto_major avg `0.6025` n `8`; equity avg `0.7773` n `102`; fx avg `0.0089` n `6`; index avg `0.0745` n `25`; metal avg `0.3902` n `20`; unknown avg `0.0024` n `739`
- 24h: commodity avg `0.5539` n `12`; crypto_alt avg `-0.3829` n `230`; crypto_major avg `-0.2369` n `8`; equity avg `-2.967` n `102`; fx avg `-0.0005` n `6`; index avg `-0.3982` n `25`; metal avg `0.328` n `20`; unknown avg `-0.1557` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
