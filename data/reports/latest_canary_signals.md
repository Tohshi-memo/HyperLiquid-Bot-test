# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T15:07:30.441493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.34` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1825` n `12`; crypto_alt avg `0.2588` n `234`; crypto_major avg `0.3439` n `8`; equity avg `0.2455` n `137`; fx avg `-0.0224` n `6`; index avg `0.0582` n `27`; metal avg `0.0294` n `20`; unknown avg `-0.0706` n `915`
- 1h: commodity avg `-0.364` n `12`; crypto_alt avg `-0.1546` n `234`; crypto_major avg `0.1929` n `8`; equity avg `0.3758` n `137`; fx avg `-0.0457` n `6`; index avg `0.0692` n `27`; metal avg `0.1884` n `20`; unknown avg `10.4286` n `915`
- 4h: commodity avg `-0.407` n `12`; crypto_alt avg `-0.7518` n `234`; crypto_major avg `-0.39` n `8`; equity avg `0.6008` n `137`; fx avg `-0.0359` n `6`; index avg `0.0933` n `27`; metal avg `0.0049` n `20`; unknown avg `19.7319` n `897`
- 24h: commodity avg `-0.5692` n `12`; crypto_alt avg `-2.5972` n `234`; crypto_major avg `-1.7693` n `8`; equity avg `1.3239` n `137`; fx avg `0.03` n `6`; index avg `0.305` n `27`; metal avg `0.553` n `20`; unknown avg `11.5978` n `806`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
