# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T15:22:29.236091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.1855` n `234`; crypto_major avg `0.0674` n `8`; equity avg `0.0181` n `141`; fx avg `0.0021` n `6`; index avg `-0.0024` n `26`; metal avg `0.0033` n `20`; unknown avg `0.8994` n `961`
- 1h: commodity avg `0.003` n `12`; crypto_alt avg `0.8139` n `234`; crypto_major avg `0.1945` n `8`; equity avg `0.0772` n `141`; fx avg `-0.0059` n `6`; index avg `0.0054` n `26`; metal avg `0.0034` n `20`; unknown avg `20.531` n `959`
- 4h: commodity avg `0.0438` n `12`; crypto_alt avg `0.6289` n `234`; crypto_major avg `0.1111` n `8`; equity avg `0.1013` n `141`; fx avg `0.0155` n `6`; index avg `0.0061` n `26`; metal avg `0.0052` n `20`; unknown avg `2.2121` n `949`
- 24h: commodity avg `0.1304` n `12`; crypto_alt avg `3.1082` n `234`; crypto_major avg `-0.1522` n `8`; equity avg `0.0899` n `141`; fx avg `0.0037` n `6`; index avg `0.0736` n `26`; metal avg `0.0703` n `20`; unknown avg `-0.5237` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
