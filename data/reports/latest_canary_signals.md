# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T19:22:31.610957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0525` n `12`; crypto_alt avg `0.0908` n `234`; crypto_major avg `0.0323` n `8`; equity avg `-0.0856` n `141`; fx avg `-0.0015` n `6`; index avg `-0.0249` n `26`; metal avg `-0.1055` n `20`; unknown avg `8.9516` n `943`
- 1h: commodity avg `0.1385` n `12`; crypto_alt avg `0.107` n `234`; crypto_major avg `0.4885` n `8`; equity avg `-0.1141` n `141`; fx avg `-0.0006` n `6`; index avg `-0.0224` n `26`; metal avg `-0.016` n `20`; unknown avg `9.996` n `941`
- 4h: commodity avg `0.188` n `12`; crypto_alt avg `-1.5473` n `234`; crypto_major avg `-0.9076` n `8`; equity avg `-0.5018` n `141`; fx avg `-0.0183` n `6`; index avg `-0.0971` n `26`; metal avg `-0.0838` n `20`; unknown avg `11.2218` n `919`
- 24h: commodity avg `0.5315` n `12`; crypto_alt avg `-3.2831` n `234`; crypto_major avg `-3.6612` n `8`; equity avg `-1.3969` n `140`; fx avg `-0.0248` n `6`; index avg `-0.3605` n `26`; metal avg `-0.8374` n `20`; unknown avg `13.0877` n `878`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
