# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T21:22:28.759381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `-0.1631` n `234`; crypto_major avg `0.0533` n `8`; equity avg `-0.003` n `141`; fx avg `-0.002` n `6`; index avg `0.0027` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.0142` n `960`
- 1h: commodity avg `-0.0395` n `12`; crypto_alt avg `-0.837` n `234`; crypto_major avg `-0.4907` n `8`; equity avg `0.0075` n `141`; fx avg `-0.0158` n `6`; index avg `0.0064` n `26`; metal avg `-0.0085` n `20`; unknown avg `-0.8242` n `928`
- 4h: commodity avg `0.1692` n `12`; crypto_alt avg `0.0635` n `234`; crypto_major avg `-0.1446` n `8`; equity avg `-0.2149` n `141`; fx avg `-0.0235` n `6`; index avg `0.0157` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.3252` n `876`
- 24h: commodity avg `-0.6548` n `12`; crypto_alt avg `1.3445` n `234`; crypto_major avg `0.219` n `8`; equity avg `0.0691` n `141`; fx avg `-0.2438` n `6`; index avg `0.2438` n `26`; metal avg `0.1659` n `20`; unknown avg `1148.2773` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
