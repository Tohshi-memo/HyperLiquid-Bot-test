# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T16:07:34.212176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `-0.122` n `237`; crypto_major avg `-0.014` n `8`; equity avg `0.0747` n `152`; fx avg `-0.0098` n `6`; index avg `0.0096` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.7654` n `1232`
- 1h: commodity avg `-0.0319` n `13`; crypto_alt avg `0.1907` n `237`; crypto_major avg `0.0088` n `8`; equity avg `0.1235` n `152`; fx avg `-0.0131` n `6`; index avg `0.0086` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.089` n `1234`
- 4h: commodity avg `-0.0756` n `13`; crypto_alt avg `0.5461` n `237`; crypto_major avg `0.2969` n `8`; equity avg `0.3483` n `152`; fx avg `-0.0139` n `6`; index avg `0.054` n `26`; metal avg `0.0482` n `20`; unknown avg `0.7988` n `1225`
- 24h: commodity avg `-0.2027` n `13`; crypto_alt avg `1.2135` n `237`; crypto_major avg `1.8111` n `8`; equity avg `1.0244` n `152`; fx avg `0.0114` n `6`; index avg `0.1703` n `26`; metal avg `0.1542` n `20`; unknown avg `18.7239` n `1081`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
