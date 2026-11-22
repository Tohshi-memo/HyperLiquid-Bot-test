# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T14:07:28.511794+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `0.2102` n `239`; crypto_major avg `0.1899` n `8`; equity avg `0.0917` n `166`; fx avg `0.0011` n `6`; index avg `0.0025` n `27`; metal avg `0.0119` n `20`; unknown avg `159.6939` n `1253`
- 1h: commodity avg `-0.0021` n `13`; crypto_alt avg `0.1855` n `239`; crypto_major avg `0.11` n `8`; equity avg `0.0446` n `166`; fx avg `0.0002` n `6`; index avg `0.034` n `27`; metal avg `-0.0015` n `20`; unknown avg `409.7527` n `1259`
- 4h: commodity avg `-0.036` n `13`; crypto_alt avg `0.1376` n `239`; crypto_major avg `-0.3176` n `8`; equity avg `0.1483` n `166`; fx avg `0.012` n `6`; index avg `0.0497` n `27`; metal avg `-0.0057` n `20`; unknown avg `160.6462` n `1253`
- 24h: commodity avg `-0.0166` n `13`; crypto_alt avg `0.7862` n `239`; crypto_major avg `0.4237` n `8`; equity avg `0.8054` n `166`; fx avg `-0.0059` n `6`; index avg `0.1375` n `27`; metal avg `-0.0077` n `20`; unknown avg `184.6006` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
