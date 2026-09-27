# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T06:07:28.669776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0177` n `234`; crypto_major avg `0.0784` n `8`; equity avg `0.011` n `141`; fx avg `0.0` n `6`; index avg `0.0006` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.0502` n `939`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `0.3799` n `234`; crypto_major avg `0.4119` n `8`; equity avg `0.0107` n `141`; fx avg `0.0075` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.5626` n `939`
- 4h: commodity avg `0.0807` n `12`; crypto_alt avg `0.0257` n `234`; crypto_major avg `-0.023` n `8`; equity avg `0.0625` n `141`; fx avg `0.0034` n `6`; index avg `0.0148` n `26`; metal avg `-0.0185` n `20`; unknown avg `0.305` n `933`
- 24h: commodity avg `0.0138` n `12`; crypto_alt avg `1.1276` n `234`; crypto_major avg `0.1804` n `8`; equity avg `0.2614` n `141`; fx avg `0.0341` n `6`; index avg `0.0043` n `26`; metal avg `-0.0191` n `20`; unknown avg `4.8265` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
