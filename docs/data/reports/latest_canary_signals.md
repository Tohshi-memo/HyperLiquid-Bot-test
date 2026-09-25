# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T03:22:31.393476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0109` n `12`; crypto_alt avg `-0.2885` n `234`; crypto_major avg `-0.1379` n `8`; equity avg `0.0016` n `141`; fx avg `0.0068` n `6`; index avg `0.0058` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.7509` n `946`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `-1.0719` n `234`; crypto_major avg `-0.8142` n `8`; equity avg `-0.0446` n `141`; fx avg `-0.0185` n `6`; index avg `0.0061` n `26`; metal avg `-0.056` n `20`; unknown avg `4.3565` n `944`
- 4h: commodity avg `-0.2211` n `12`; crypto_alt avg `-0.9311` n `234`; crypto_major avg `-0.3954` n `8`; equity avg `0.3696` n `141`; fx avg `-0.1463` n `6`; index avg `0.1074` n `26`; metal avg `-0.0056` n `20`; unknown avg `2.1923` n `938`
- 24h: commodity avg `0.4632` n `12`; crypto_alt avg `1.7642` n `234`; crypto_major avg `0.6417` n `8`; equity avg `0.3075` n `141`; fx avg `-0.129` n `6`; index avg `0.0324` n `26`; metal avg `-0.0731` n `20`; unknown avg `22.4742` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
