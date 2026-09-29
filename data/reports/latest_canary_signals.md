# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T14:52:31.371065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `0.0986` n `234`; crypto_major avg `0.0422` n `8`; equity avg `-0.084` n `141`; fx avg `0.0083` n `6`; index avg `0.0182` n `26`; metal avg `0.0394` n `20`; unknown avg `2.9151` n `959`
- 1h: commodity avg `0.1317` n `12`; crypto_alt avg `0.2061` n `234`; crypto_major avg `-0.3885` n `8`; equity avg `0.4878` n `141`; fx avg `-0.0045` n `6`; index avg `0.0649` n `26`; metal avg `0.0513` n `20`; unknown avg `220.1479` n `909`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `1.0569` n `234`; crypto_major avg `0.432` n `8`; equity avg `0.7124` n `141`; fx avg `-0.0031` n `6`; index avg `0.0692` n `26`; metal avg `0.0486` n `20`; unknown avg `227.1627` n `903`
- 24h: commodity avg `-0.8317` n `12`; crypto_alt avg `3.8941` n `234`; crypto_major avg `2.0546` n `8`; equity avg `1.9866` n `141`; fx avg `-0.1164` n `6`; index avg `0.2504` n `26`; metal avg `0.1412` n `20`; unknown avg `14.4275` n `796`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
