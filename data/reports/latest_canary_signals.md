# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T09:22:30.615058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0822` n `13`; crypto_alt avg `-0.0484` n `237`; crypto_major avg `-0.0526` n `8`; equity avg `-0.1378` n `152`; fx avg `-0.0164` n `6`; index avg `-0.0169` n `26`; metal avg `0.0107` n `20`; unknown avg `0.0693` n `1221`
- 1h: commodity avg `0.0534` n `13`; crypto_alt avg `-0.0531` n `237`; crypto_major avg `-0.1154` n `8`; equity avg `-0.3882` n `152`; fx avg `-0.0606` n `6`; index avg `-0.0742` n `26`; metal avg `0.0352` n `20`; unknown avg `0.4917` n `1207`
- 4h: commodity avg `0.0948` n `13`; crypto_alt avg `0.1468` n `237`; crypto_major avg `0.3077` n `8`; equity avg `0.7415` n `152`; fx avg `-0.0694` n `6`; index avg `0.0327` n `26`; metal avg `0.0309` n `20`; unknown avg `0.0298` n `1134`
- 24h: commodity avg `0.3393` n `13`; crypto_alt avg `0.2027` n `237`; crypto_major avg `0.4764` n `8`; equity avg `-0.7012` n `152`; fx avg `-0.0994` n `6`; index avg `-0.0797` n `26`; metal avg `-0.3697` n `20`; unknown avg `51.1549` n `918`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
