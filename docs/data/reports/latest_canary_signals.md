# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T19:07:30.218887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `13`; crypto_alt avg `0.0637` n `238`; crypto_major avg `0.1317` n `8`; equity avg `0.146` n `154`; fx avg `0.0046` n `6`; index avg `0.0293` n `27`; metal avg `0.0465` n `20`; unknown avg `0.8224` n `1232`
- 1h: commodity avg `-0.0666` n `13`; crypto_alt avg `0.2254` n `238`; crypto_major avg `0.1956` n `8`; equity avg `0.2238` n `154`; fx avg `0.0015` n `6`; index avg `0.0183` n `27`; metal avg `0.0158` n `20`; unknown avg `1.4095` n `1230`
- 4h: commodity avg `-0.0997` n `13`; crypto_alt avg `0.8977` n `238`; crypto_major avg `0.862` n `8`; equity avg `0.7407` n `154`; fx avg `-0.0074` n `6`; index avg `0.0807` n `27`; metal avg `-0.0084` n `20`; unknown avg `8.0932` n `1196`
- 24h: commodity avg `-0.5761` n `13`; crypto_alt avg `1.2791` n `237`; crypto_major avg `1.4167` n `8`; equity avg `1.7235` n `154`; fx avg `-0.0553` n `6`; index avg `0.4285` n `27`; metal avg `0.204` n `20`; unknown avg `28.7208` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
