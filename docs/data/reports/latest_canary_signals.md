# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T14:37:34.199816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `0.053` n `234`; crypto_major avg `0.0583` n `8`; equity avg `0.053` n `137`; fx avg `0.0121` n `6`; index avg `-0.0106` n `27`; metal avg `0.0487` n `20`; unknown avg `10.6194` n `917`
- 1h: commodity avg `-0.1479` n `12`; crypto_alt avg `-0.4831` n `234`; crypto_major avg `0.0555` n `8`; equity avg `0.3182` n `137`; fx avg `-0.0046` n `6`; index avg `0.0095` n `27`; metal avg `-0.0012` n `20`; unknown avg `0.3049` n `903`
- 4h: commodity avg `-0.2099` n `12`; crypto_alt avg `-0.7454` n `234`; crypto_major avg `-0.3804` n `8`; equity avg `0.4174` n `137`; fx avg `0.0009` n `6`; index avg `0.0294` n `27`; metal avg `-0.0593` n `20`; unknown avg `0.213` n `897`
- 24h: commodity avg `-0.2238` n `12`; crypto_alt avg `-2.8359` n `234`; crypto_major avg `-2.1502` n `8`; equity avg `0.7975` n `137`; fx avg `0.079` n `6`; index avg `0.1887` n `27`; metal avg `0.4218` n `20`; unknown avg `3.291` n `794`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
