# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T04:30:12.924242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0386` n `232`; crypto_major avg `0.0296` n `8`; equity avg `0.0114` n `134`; fx avg `-0.0043` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.6931` n `786`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `-0.3809` n `232`; crypto_major avg `-0.2614` n `8`; equity avg `-0.0224` n `134`; fx avg `-0.0129` n `6`; index avg `0.0099` n `26`; metal avg `-0.0091` n `20`; unknown avg `0.3754` n `752`
- 4h: commodity avg `0.0079` n `12`; crypto_alt avg `0.101` n `232`; crypto_major avg `0.468` n `8`; equity avg `0.0835` n `134`; fx avg `-0.0055` n `6`; index avg `0.0122` n `26`; metal avg `-0.0162` n `20`; unknown avg `1.2778` n `752`
- 24h: commodity avg `0.1029` n `12`; crypto_alt avg `2.8194` n `232`; crypto_major avg `2.9412` n `8`; equity avg `0.4783` n `134`; fx avg `-0.0667` n `6`; index avg `0.1133` n `26`; metal avg `0.0254` n `20`; unknown avg `1.2514` n `680`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
