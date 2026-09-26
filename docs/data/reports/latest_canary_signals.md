# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T13:37:30.901213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.0483` n `234`; crypto_major avg `-0.044` n `8`; equity avg `-0.0097` n `141`; fx avg `-0.0021` n `6`; index avg `0.0005` n `26`; metal avg `0.0034` n `20`; unknown avg `-0.1213` n `961`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.1458` n `234`; crypto_major avg `-0.1911` n `8`; equity avg `-0.0063` n `141`; fx avg `0.0034` n `6`; index avg `-0.0022` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.1151` n `959`
- 4h: commodity avg `0.0286` n `12`; crypto_alt avg `0.475` n `234`; crypto_major avg `0.1154` n `8`; equity avg `0.0684` n `141`; fx avg `0.0221` n `6`; index avg `-0.0104` n `26`; metal avg `0.0014` n `20`; unknown avg `1.326` n `949`
- 24h: commodity avg `0.1483` n `12`; crypto_alt avg `1.7124` n `234`; crypto_major avg `-0.773` n `8`; equity avg `-0.4533` n `141`; fx avg `0.016` n `6`; index avg `0.02` n `26`; metal avg `0.0914` n `20`; unknown avg `1119.3577` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
