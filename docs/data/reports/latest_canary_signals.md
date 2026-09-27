# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T07:22:27.239921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.0419` n `234`; crypto_major avg `0.0604` n `8`; equity avg `0.0191` n `141`; fx avg `-0.0002` n `6`; index avg `0.0007` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.0128` n `961`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.3183` n `234`; crypto_major avg `-0.0042` n `8`; equity avg `0.0406` n `141`; fx avg `-0.0047` n `6`; index avg `0.0042` n `26`; metal avg `0.0143` n `20`; unknown avg `-0.014` n `959`
- 4h: commodity avg `0.0132` n `12`; crypto_alt avg `0.8162` n `234`; crypto_major avg `0.319` n `8`; equity avg `0.0863` n `141`; fx avg `0.0106` n `6`; index avg `0.0132` n `26`; metal avg `0.002` n `20`; unknown avg `24.9532` n `933`
- 24h: commodity avg `0.0315` n `12`; crypto_alt avg `0.8803` n `234`; crypto_major avg `0.1294` n `8`; equity avg `0.3034` n `141`; fx avg `0.0124` n `6`; index avg `0.0087` n `26`; metal avg `-0.0046` n `20`; unknown avg `4.8307` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
