# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T19:22:26.243679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0708` n `12`; crypto_alt avg `0.2051` n `234`; crypto_major avg `0.1467` n `8`; equity avg `0.0045` n `141`; fx avg `0.0013` n `6`; index avg `-0.005` n `26`; metal avg `-0.0036` n `20`; unknown avg `1.5234` n `943`
- 1h: commodity avg `0.1663` n `12`; crypto_alt avg `0.5523` n `234`; crypto_major avg `0.3015` n `8`; equity avg `0.1812` n `141`; fx avg `0.0074` n `6`; index avg `0.0122` n `26`; metal avg `0.0192` n `20`; unknown avg `26.8149` n `939`
- 4h: commodity avg `0.1431` n `12`; crypto_alt avg `1.3699` n `234`; crypto_major avg `1.152` n `8`; equity avg `0.9342` n `141`; fx avg `-0.0093` n `6`; index avg `0.1262` n `26`; metal avg `0.1646` n `20`; unknown avg `9.6347` n `927`
- 24h: commodity avg `1.0505` n `12`; crypto_alt avg `3.8255` n `234`; crypto_major avg `1.6363` n `8`; equity avg `-0.3089` n `141`; fx avg `0.0501` n `6`; index avg `-0.09` n `26`; metal avg `-0.0554` n `20`; unknown avg `266.9692` n `831`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
