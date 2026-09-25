# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T14:22:36.489198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0593` n `12`; crypto_alt avg `0.4258` n `234`; crypto_major avg `0.3034` n `8`; equity avg `-0.1879` n `141`; fx avg `0.0227` n `6`; index avg `-0.0342` n `26`; metal avg `0.0568` n `20`; unknown avg `11.0432` n `960`
- 1h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.7767` n `234`; crypto_major avg `-0.574` n `8`; equity avg `-1.1361` n `141`; fx avg `0.0366` n `6`; index avg `-0.1054` n `26`; metal avg `-0.1496` n `20`; unknown avg `86.6546` n `922`
- 4h: commodity avg `-0.0861` n `12`; crypto_alt avg `-0.0047` n `234`; crypto_major avg `0.1942` n `8`; equity avg `-1.2467` n `141`; fx avg `-0.0144` n `6`; index avg `-0.1389` n `26`; metal avg `-0.3139` n `20`; unknown avg `10.4722` n `916`
- 24h: commodity avg `-0.1705` n `12`; crypto_alt avg `1.8676` n `234`; crypto_major avg `1.2486` n `8`; equity avg `0.2221` n `141`; fx avg `-0.2138` n `6`; index avg `0.1135` n `26`; metal avg `-0.0124` n `20`; unknown avg `9.2884` n `801`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
