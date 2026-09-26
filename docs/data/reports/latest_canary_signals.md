# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T13:52:29.309294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `0.2014` n `234`; crypto_major avg `0.0296` n `8`; equity avg `0.0117` n `141`; fx avg `0.0013` n `6`; index avg `0.0044` n `26`; metal avg `-0.0001` n `20`; unknown avg `3.4948` n `961`
- 1h: commodity avg `0.0071` n `12`; crypto_alt avg `0.0871` n `234`; crypto_major avg `-0.158` n `8`; equity avg `0.0072` n `141`; fx avg `0.0016` n `6`; index avg `0.0101` n `26`; metal avg `0.0012` n `20`; unknown avg `3.2852` n `959`
- 4h: commodity avg `0.0495` n `12`; crypto_alt avg `0.5092` n `234`; crypto_major avg `0.1167` n `8`; equity avg `0.0768` n `141`; fx avg `0.0221` n `6`; index avg `-0.0042` n `26`; metal avg `0.0048` n `20`; unknown avg `3.3668` n `949`
- 24h: commodity avg `0.2295` n `12`; crypto_alt avg `2.3757` n `234`; crypto_major avg `-0.326` n `8`; equity avg `-0.194` n `141`; fx avg `0.0281` n `6`; index avg `0.033` n `26`; metal avg `0.1065` n `20`; unknown avg `1119.2065` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
