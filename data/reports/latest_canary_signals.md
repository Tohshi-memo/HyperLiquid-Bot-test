# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T01:52:30.324482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0398` n `12`; crypto_alt avg `-0.2359` n `234`; crypto_major avg `-0.4108` n `8`; equity avg `-0.096` n `141`; fx avg `0.01` n `6`; index avg `-0.0234` n `26`; metal avg `-0.0087` n `20`; unknown avg `0.2179` n `945`
- 1h: commodity avg `0.0576` n `12`; crypto_alt avg `0.0991` n `234`; crypto_major avg `-0.2313` n `8`; equity avg `0.0491` n `141`; fx avg `-0.0602` n `6`; index avg `-0.0003` n `26`; metal avg `0.0082` n `20`; unknown avg `0.5551` n `943`
- 4h: commodity avg `-0.095` n `12`; crypto_alt avg `0.1049` n `234`; crypto_major avg `-0.1651` n `8`; equity avg `-0.1918` n `141`; fx avg `0.0239` n `6`; index avg `-0.0392` n `26`; metal avg `-0.071` n `20`; unknown avg `0.2686` n `937`
- 24h: commodity avg `0.4237` n `12`; crypto_alt avg `-4.1084` n `234`; crypto_major avg `-3.6366` n `8`; equity avg `-1.5626` n `140`; fx avg `0.1114` n `6`; index avg `-0.3126` n `26`; metal avg `-0.6869` n `20`; unknown avg `583.2713` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
