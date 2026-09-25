# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T14:37:32.654476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `0.3719` n `234`; crypto_major avg `0.2328` n `8`; equity avg `0.1116` n `141`; fx avg `0.0044` n `6`; index avg `0.01` n `26`; metal avg `0.043` n `20`; unknown avg `0.2468` n `960`
- 1h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.2792` n `234`; crypto_major avg `-0.2395` n `8`; equity avg `-0.7174` n `141`; fx avg `0.0352` n `6`; index avg `-0.0961` n `26`; metal avg `-0.0902` n `20`; unknown avg `11.2094` n `922`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `0.0937` n `234`; crypto_major avg `0.0047` n `8`; equity avg `-1.123` n `141`; fx avg `-0.0018` n `6`; index avg `-0.1087` n `26`; metal avg `-0.2558` n `20`; unknown avg `12.9976` n `916`
- 24h: commodity avg `-0.1422` n `12`; crypto_alt avg `1.5659` n `234`; crypto_major avg `0.956` n `8`; equity avg `0.1045` n `141`; fx avg `-0.2032` n `6`; index avg `0.1039` n `26`; metal avg `0.0284` n `20`; unknown avg `7.7555` n `801`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
