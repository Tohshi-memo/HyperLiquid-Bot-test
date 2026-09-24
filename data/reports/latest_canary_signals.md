# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T01:37:28.942539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `0.3257` n `234`; crypto_major avg `0.198` n `8`; equity avg `0.1016` n `141`; fx avg `0.0031` n `6`; index avg `0.008` n `26`; metal avg `-0.009` n `20`; unknown avg `0.1647` n `945`
- 1h: commodity avg `0.0303` n `12`; crypto_alt avg `0.1076` n `234`; crypto_major avg `-0.053` n `8`; equity avg `-0.0541` n `141`; fx avg `0.0085` n `6`; index avg `0.008` n `26`; metal avg `0.0126` n `20`; unknown avg `0.5463` n `943`
- 4h: commodity avg `-0.1494` n `12`; crypto_alt avg `0.1617` n `234`; crypto_major avg `0.2869` n `8`; equity avg `-0.0682` n `141`; fx avg `0.0126` n `6`; index avg `-0.0138` n `26`; metal avg `-0.0378` n `20`; unknown avg `0.2166` n `937`
- 24h: commodity avg `0.3712` n `12`; crypto_alt avg `-4.305` n `234`; crypto_major avg `-3.4626` n `8`; equity avg `-1.5812` n `140`; fx avg `0.1075` n `6`; index avg `-0.3024` n `26`; metal avg `-0.7232` n `20`; unknown avg `583.4116` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
