# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T13:37:32.139195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0959` n `13`; crypto_alt avg `0.1702` n `237`; crypto_major avg `-0.0594` n `8`; equity avg `-0.1235` n `152`; fx avg `-0.0068` n `6`; index avg `0.0641` n `26`; metal avg `-0.0261` n `20`; unknown avg `2.1757` n `1240`
- 1h: commodity avg `0.0042` n `13`; crypto_alt avg `-0.1201` n `237`; crypto_major avg `-0.3875` n `8`; equity avg `-0.4675` n `152`; fx avg `-0.0105` n `6`; index avg `0.0184` n `26`; metal avg `-0.1481` n `20`; unknown avg `5.4556` n `1220`
- 4h: commodity avg `0.0429` n `13`; crypto_alt avg `0.0154` n `237`; crypto_major avg `-0.1721` n `8`; equity avg `-0.0606` n `152`; fx avg `-0.0093` n `6`; index avg `0.0518` n `26`; metal avg `-0.1316` n `20`; unknown avg `10.8401` n `1214`
- 24h: commodity avg `-0.2913` n `13`; crypto_alt avg `0.4529` n `237`; crypto_major avg `0.1352` n `8`; equity avg `-0.3719` n `152`; fx avg `0.0298` n `6`; index avg `0.0771` n `26`; metal avg `0.059` n `20`; unknown avg `0.1854` n `959`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
