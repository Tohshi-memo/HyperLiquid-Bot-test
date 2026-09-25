# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T05:22:27.978330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0342` n `12`; crypto_alt avg `-0.0732` n `234`; crypto_major avg `-0.0284` n `8`; equity avg `0.0122` n `141`; fx avg `-0.0194` n `6`; index avg `0.0073` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.0119` n `944`
- 1h: commodity avg `0.0385` n `12`; crypto_alt avg `-0.1409` n `234`; crypto_major avg `-0.0226` n `8`; equity avg `0.0978` n `141`; fx avg `-0.014` n `6`; index avg `0.0261` n `26`; metal avg `-0.049` n `20`; unknown avg `26.315` n `942`
- 4h: commodity avg `0.0302` n `12`; crypto_alt avg `-0.9406` n `234`; crypto_major avg `-0.6525` n `8`; equity avg `0.0211` n `141`; fx avg `-0.0997` n `6`; index avg `0.0292` n `26`; metal avg `-0.2358` n `20`; unknown avg `6.391` n `936`
- 24h: commodity avg `0.5131` n `12`; crypto_alt avg `1.2342` n `234`; crypto_major avg `0.0836` n `8`; equity avg `0.4663` n `141`; fx avg `-0.1265` n `6`; index avg `0.0516` n `26`; metal avg `-0.2538` n `20`; unknown avg `17.5108` n `813`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
