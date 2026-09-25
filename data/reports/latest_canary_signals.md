# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T17:52:27.650392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.1268` n `234`; crypto_major avg `0.03` n `8`; equity avg `0.0269` n `141`; fx avg `-0.0013` n `6`; index avg `0.0138` n `26`; metal avg `0.0167` n `20`; unknown avg `0.2177` n `960`
- 1h: commodity avg `0.0465` n `12`; crypto_alt avg `-0.2609` n `234`; crypto_major avg `-0.363` n `8`; equity avg `-0.0841` n `141`; fx avg `-0.0017` n `6`; index avg `0.0116` n `26`; metal avg `-0.0093` n `20`; unknown avg `-0.0019` n `958`
- 4h: commodity avg `-0.1403` n `12`; crypto_alt avg `0.2599` n `234`; crypto_major avg `-0.3093` n `8`; equity avg `-0.062` n `141`; fx avg `0.0089` n `6`; index avg `0.0565` n `26`; metal avg `0.1022` n `20`; unknown avg `4.3721` n `894`
- 24h: commodity avg `-0.9973` n `12`; crypto_alt avg `1.7234` n `234`; crypto_major avg `0.4987` n `8`; equity avg `0.2515` n `141`; fx avg `-0.2429` n `6`; index avg `0.2312` n `26`; metal avg `0.2045` n `20`; unknown avg `1601.7964` n `805`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
