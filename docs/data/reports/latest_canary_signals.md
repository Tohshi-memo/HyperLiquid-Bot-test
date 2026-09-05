# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T13:22:24.372844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.0521` n `232`; crypto_major avg `0.1252` n `8`; equity avg `-0.0017` n `134`; fx avg `0.0115` n `6`; index avg `-0.0035` n `26`; metal avg `0.0026` n `20`; unknown avg `0.0677` n `794`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.3587` n `232`; crypto_major avg `0.7366` n `8`; equity avg `0.009` n `134`; fx avg `0.0106` n `6`; index avg `0.0126` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.0851` n `784`
- 4h: commodity avg `0.0002` n `12`; crypto_alt avg `0.4487` n `232`; crypto_major avg `0.7731` n `8`; equity avg `0.0758` n `134`; fx avg `-0.0039` n `6`; index avg `0.0427` n `26`; metal avg `-0.0099` n `20`; unknown avg `-0.1267` n `780`
- 24h: commodity avg `0.1519` n `12`; crypto_alt avg `2.8908` n `232`; crypto_major avg `1.6301` n `8`; equity avg `1.64` n `134`; fx avg `0.0382` n `6`; index avg `0.1957` n `26`; metal avg `0.1955` n `20`; unknown avg `15.9322` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
