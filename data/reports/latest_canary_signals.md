# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T05:07:28.990873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.2032` n `234`; crypto_major avg `-0.1388` n `8`; equity avg `0.0259` n `141`; fx avg `0.0027` n `6`; index avg `0.0028` n `26`; metal avg `-0.0504` n `20`; unknown avg `0.9211` n `944`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `0.0192` n `234`; crypto_major avg `-0.1192` n `8`; equity avg `0.095` n `141`; fx avg `0.0205` n `6`; index avg `0.014` n `26`; metal avg `-0.046` n `20`; unknown avg `17.393` n `944`
- 4h: commodity avg `-0.0357` n `12`; crypto_alt avg `-1.0041` n `234`; crypto_major avg `-0.7488` n `8`; equity avg `0.2665` n `141`; fx avg `-0.103` n `6`; index avg `0.0789` n `26`; metal avg `-0.1529` n `20`; unknown avg `7.514` n `938`
- 24h: commodity avg `0.5301` n `12`; crypto_alt avg `1.0397` n `234`; crypto_major avg `-0.1573` n `8`; equity avg `0.3436` n `141`; fx avg `-0.11` n `6`; index avg `0.0291` n `26`; metal avg `-0.2797` n `20`; unknown avg `17.4503` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
