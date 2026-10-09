# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T09:22:27.022203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `0.0072` n `235`; crypto_major avg `-0.0136` n `8`; equity avg `-0.0717` n `150`; fx avg `0.0065` n `6`; index avg `-0.0056` n `26`; metal avg `0.0093` n `20`; unknown avg `0.7193` n `1078`
- 1h: commodity avg `0.0684` n `13`; crypto_alt avg `-0.0172` n `235`; crypto_major avg `-0.0929` n `8`; equity avg `-0.1514` n `150`; fx avg `-0.0441` n `6`; index avg `-0.0139` n `26`; metal avg `-0.099` n `20`; unknown avg `0.0272` n `1076`
- 4h: commodity avg `-0.0525` n `13`; crypto_alt avg `0.2834` n `235`; crypto_major avg `0.0919` n `8`; equity avg `0.3028` n `150`; fx avg `0.003` n `6`; index avg `0.0566` n `26`; metal avg `0.0525` n `20`; unknown avg `1.9417` n `988`
- 24h: commodity avg `-0.3961` n `13`; crypto_alt avg `-1.2398` n `235`; crypto_major avg `-1.9201` n `8`; equity avg `-0.4782` n `150`; fx avg `0.0769` n `6`; index avg `0.0636` n `26`; metal avg `0.4553` n `20`; unknown avg `7.4531` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
