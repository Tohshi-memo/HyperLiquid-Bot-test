# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T14:37:28.272474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `0.1764` n `234`; crypto_major avg `0.0708` n `8`; equity avg `0.0192` n `141`; fx avg `0.0006` n `6`; index avg `0.0016` n `26`; metal avg `0.0035` n `20`; unknown avg `1.8762` n `961`
- 1h: commodity avg `0.0621` n `12`; crypto_alt avg `0.4771` n `234`; crypto_major avg `0.2644` n `8`; equity avg `0.042` n `141`; fx avg `0.0032` n `6`; index avg `0.0115` n `26`; metal avg `0.0036` n `20`; unknown avg `3.627` n `959`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `0.24` n `234`; crypto_major avg `0.0442` n `8`; equity avg `0.0649` n `141`; fx avg `0.02` n `6`; index avg `0.0058` n `26`; metal avg `0.0042` n `20`; unknown avg `1.5696` n `949`
- 24h: commodity avg `0.2359` n `12`; crypto_alt avg `2.4847` n `234`; crypto_major avg `-0.2737` n `8`; equity avg `0.3099` n `141`; fx avg `-0.016` n `6`; index avg `0.1283` n `26`; metal avg `0.1857` n `20`; unknown avg `2.1089` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
