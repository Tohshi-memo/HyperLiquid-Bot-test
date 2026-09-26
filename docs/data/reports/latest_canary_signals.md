# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T22:52:27.481922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0897` n `234`; crypto_major avg `0.0503` n `8`; equity avg `0.0276` n `141`; fx avg `0.0075` n `6`; index avg `0.0002` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.0762` n `961`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `0.1967` n `234`; crypto_major avg `0.0897` n `8`; equity avg `0.0587` n `141`; fx avg `-0.0002` n `6`; index avg `0.0033` n `26`; metal avg `-0.002` n `20`; unknown avg `2.7923` n `935`
- 4h: commodity avg `0.039` n `12`; crypto_alt avg `-0.3038` n `234`; crypto_major avg `0.1354` n `8`; equity avg `0.0618` n `141`; fx avg `-0.0135` n `6`; index avg `-0.004` n `26`; metal avg `0.009` n `20`; unknown avg `162.4621` n `929`
- 24h: commodity avg `0.3309` n `12`; crypto_alt avg `0.389` n `234`; crypto_major avg `-1.036` n `8`; equity avg `-0.0031` n `141`; fx avg `0.0124` n `6`; index avg `-0.0516` n `26`; metal avg `-0.0304` n `20`; unknown avg `4.2851` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
