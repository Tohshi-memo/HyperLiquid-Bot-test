# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T03:37:26.047454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.067` n `12`; crypto_alt avg `0.1251` n `234`; crypto_major avg `0.0288` n `8`; equity avg `-0.0088` n `141`; fx avg `-0.0106` n `6`; index avg `-0.0086` n `26`; metal avg `-0.062` n `20`; unknown avg `-0.0713` n `946`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `-0.2788` n `234`; crypto_major avg `-0.2659` n `8`; equity avg `0.1011` n `141`; fx avg `-0.0196` n `6`; index avg `0.0177` n `26`; metal avg `-0.0436` n `20`; unknown avg `1.9504` n `944`
- 4h: commodity avg `-0.1578` n `12`; crypto_alt avg `-0.8616` n `234`; crypto_major avg `-0.4751` n `8`; equity avg `0.3553` n `141`; fx avg `-0.1577` n `6`; index avg `0.0763` n `26`; metal avg `-0.0647` n `20`; unknown avg `0.3127` n `938`
- 24h: commodity avg `0.5247` n `12`; crypto_alt avg `2.2411` n `234`; crypto_major avg `0.8248` n `8`; equity avg `0.4163` n `141`; fx avg `-0.1445` n `6`; index avg `0.0279` n `26`; metal avg `-0.1073` n `20`; unknown avg `18.5259` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
