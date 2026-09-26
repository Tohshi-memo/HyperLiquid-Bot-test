# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T13:07:24.961462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `0.2613` n `234`; crypto_major avg `0.1391` n `8`; equity avg `0.016` n `141`; fx avg `0.0082` n `6`; index avg `0.0007` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.0408` n `959`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0158` n `234`; crypto_major avg `0.0111` n `8`; equity avg `0.0124` n `141`; fx avg `0.0093` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0047` n `20`; unknown avg `0.6823` n `959`
- 4h: commodity avg `0.0159` n `12`; crypto_alt avg `0.5033` n `234`; crypto_major avg `0.0974` n `8`; equity avg `0.0203` n `141`; fx avg `0.0285` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0048` n `20`; unknown avg `2.4917` n `949`
- 24h: commodity avg `0.1355` n `12`; crypto_alt avg `1.5588` n `234`; crypto_major avg `-0.9588` n `8`; equity avg `-0.8366` n `141`; fx avg `-0.0148` n `6`; index avg `0.0015` n `26`; metal avg `0.0144` n `20`; unknown avg `1121.2853` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
