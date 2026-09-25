# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T13:07:29.206578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.3496` n `234`; crypto_major avg `0.0886` n `8`; equity avg `0.0931` n `141`; fx avg `-0.0232` n `6`; index avg `0.0113` n `26`; metal avg `-0.0145` n `20`; unknown avg `93.3694` n `942`
- 1h: commodity avg `0.0938` n `12`; crypto_alt avg `0.0847` n `234`; crypto_major avg `-0.2539` n `8`; equity avg `-0.0409` n `141`; fx avg `0.0007` n `6`; index avg `-0.0329` n `26`; metal avg `-0.0991` n `20`; unknown avg `27.1258` n `942`
- 4h: commodity avg `0.1018` n `12`; crypto_alt avg `1.0813` n `234`; crypto_major avg `1.0404` n `8`; equity avg `-0.1052` n `141`; fx avg `-0.0045` n `6`; index avg `-0.0378` n `26`; metal avg `0.0001` n `20`; unknown avg `4.0768` n `936`
- 24h: commodity avg `0.0771` n `12`; crypto_alt avg `5.1267` n `234`; crypto_major avg `3.2464` n `8`; equity avg `1.8122` n `141`; fx avg `-0.1682` n `6`; index avg `0.25` n `26`; metal avg `0.152` n `20`; unknown avg `13.4077` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
