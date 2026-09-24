# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T23:22:28.837877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.0994` n `234`; crypto_major avg `-0.0231` n `8`; equity avg `-0.0295` n `141`; fx avg `0.0139` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0124` n `20`; unknown avg `-0.0904` n `946`
- 1h: commodity avg `-0.0836` n `12`; crypto_alt avg `0.3948` n `234`; crypto_major avg `0.3376` n `8`; equity avg `0.0154` n `141`; fx avg `0.0392` n `6`; index avg `-0.014` n `26`; metal avg `0.0293` n `20`; unknown avg `3.3376` n `944`
- 4h: commodity avg `-0.484` n `12`; crypto_alt avg `-0.1036` n `234`; crypto_major avg `-0.5175` n `8`; equity avg `-0.0863` n `141`; fx avg `-0.006` n `6`; index avg `-0.0313` n `26`; metal avg `-0.0163` n `20`; unknown avg `9.5794` n `830`
- 24h: commodity avg `0.5987` n `12`; crypto_alt avg `3.7203` n `234`; crypto_major avg `0.9169` n `8`; equity avg `-0.3307` n `141`; fx avg `0.055` n `6`; index avg `-0.124` n `26`; metal avg `-0.1226` n `20`; unknown avg `22.7005` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
