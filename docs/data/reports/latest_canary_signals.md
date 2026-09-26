# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T04:52:29.386449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.3315` n `234`; crypto_major avg `0.1545` n `8`; equity avg `0.0298` n `141`; fx avg `-0.0045` n `6`; index avg `0.0047` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0976` n `961`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `0.344` n `234`; crypto_major avg `0.0493` n `8`; equity avg `0.0255` n `141`; fx avg `-0.0003` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0082` n `20`; unknown avg `17.1464` n `953`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `0.1154` n `234`; crypto_major avg `-0.1733` n `8`; equity avg `0.0597` n `141`; fx avg `0.0004` n `6`; index avg `0.0241` n `26`; metal avg `0.0082` n `20`; unknown avg `14.4221` n `952`
- 24h: commodity avg `0.0466` n `12`; crypto_alt avg `3.1553` n `234`; crypto_major avg `1.0278` n `8`; equity avg `-0.3701` n `141`; fx avg `-0.1141` n `6`; index avg `0.1243` n `26`; metal avg `0.2413` n `20`; unknown avg `1125.314` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
