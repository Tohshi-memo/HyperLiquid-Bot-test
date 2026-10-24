# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T23:37:33.103097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `0.4634` n `237`; crypto_major avg `0.4598` n `8`; equity avg `0.06` n `152`; fx avg `0.0038` n `6`; index avg `0.0037` n `26`; metal avg `0.0131` n `20`; unknown avg `0.4042` n `1231`
- 1h: commodity avg `-0.0436` n `13`; crypto_alt avg `0.4481` n `237`; crypto_major avg `0.4215` n `8`; equity avg `0.0755` n `152`; fx avg `0.0017` n `6`; index avg `0.0041` n `26`; metal avg `0.0191` n `20`; unknown avg `0.2071` n `1229`
- 4h: commodity avg `-0.0167` n `13`; crypto_alt avg `1.008` n `237`; crypto_major avg `0.7508` n `8`; equity avg `0.1328` n `152`; fx avg `0.0163` n `6`; index avg `0.0157` n `26`; metal avg `0.0175` n `20`; unknown avg `0.4778` n `1143`
- 24h: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.1787` n `237`; crypto_major avg `-0.1222` n `8`; equity avg `0.1347` n `152`; fx avg `-0.0403` n `6`; index avg `0.0107` n `26`; metal avg `-0.0729` n `20`; unknown avg `0.5659` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
