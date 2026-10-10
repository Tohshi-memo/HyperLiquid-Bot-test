# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T22:07:28.409606+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1543` n `13`; crypto_alt avg `-0.0625` n `235`; crypto_major avg `-0.0515` n `8`; equity avg `0.0176` n `150`; fx avg `0.0007` n `6`; index avg `0.0052` n `26`; metal avg `0.0096` n `20`; unknown avg `0.0121` n `1115`
- 1h: commodity avg `0.2951` n `13`; crypto_alt avg `-0.1288` n `235`; crypto_major avg `-0.1018` n `8`; equity avg `0.0207` n `150`; fx avg `-0.0002` n `6`; index avg `-0.0026` n `26`; metal avg `0.012` n `20`; unknown avg `0.868` n `1099`
- 4h: commodity avg `0.3185` n `13`; crypto_alt avg `0.4704` n `235`; crypto_major avg `0.0183` n `8`; equity avg `0.0757` n `150`; fx avg `-0.0005` n `6`; index avg `0.0066` n `26`; metal avg `0.0224` n `20`; unknown avg `0.5924` n `991`
- 24h: commodity avg `0.1856` n `13`; crypto_alt avg `2.8372` n `235`; crypto_major avg `0.9731` n `8`; equity avg `0.2276` n `150`; fx avg `-0.0091` n `6`; index avg `0.0162` n `26`; metal avg `0.0149` n `20`; unknown avg `0.6725` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
