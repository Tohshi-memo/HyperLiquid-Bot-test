# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T08:22:30.814760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `13`; crypto_alt avg `0.1596` n `237`; crypto_major avg `0.2193` n `8`; equity avg `0.3981` n `152`; fx avg `0.0077` n `6`; index avg `0.0528` n `26`; metal avg `0.0512` n `20`; unknown avg `0.0679` n `1227`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0375` n `237`; crypto_major avg `0.2314` n `8`; equity avg `0.3964` n `152`; fx avg `0.0096` n `6`; index avg `0.0515` n `26`; metal avg `0.0498` n `20`; unknown avg `0.0201` n `1165`
- 4h: commodity avg `0.0928` n `13`; crypto_alt avg `0.4165` n `237`; crypto_major avg `0.5603` n `8`; equity avg `1.5678` n `152`; fx avg `-0.0008` n `6`; index avg `0.1266` n `26`; metal avg `0.093` n `20`; unknown avg `0.1796` n `1148`
- 24h: commodity avg `0.1948` n `13`; crypto_alt avg `0.1459` n `237`; crypto_major avg `0.3669` n `8`; equity avg `-0.3527` n `152`; fx avg `-0.0623` n `6`; index avg `-0.0091` n `26`; metal avg `-0.4398` n `20`; unknown avg `54.7697` n `858`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
