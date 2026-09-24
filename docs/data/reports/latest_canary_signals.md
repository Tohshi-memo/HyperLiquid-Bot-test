# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T17:22:37.313166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1511` n `12`; crypto_alt avg `0.0241` n `234`; crypto_major avg `0.0233` n `8`; equity avg `-0.1675` n `141`; fx avg `-0.001` n `6`; index avg `-0.0409` n `26`; metal avg `-0.0474` n `20`; unknown avg `1.1367` n `943`
- 1h: commodity avg `0.1218` n `12`; crypto_alt avg `-0.1847` n `234`; crypto_major avg `-0.2525` n `8`; equity avg `0.1908` n `141`; fx avg `-0.0047` n `6`; index avg `0.0071` n `26`; metal avg `-0.045` n `20`; unknown avg `7.2479` n `941`
- 4h: commodity avg `0.7092` n `12`; crypto_alt avg `2.3442` n `234`; crypto_major avg `1.3893` n `8`; equity avg `1.0031` n `141`; fx avg `0.0185` n `6`; index avg `0.1017` n `26`; metal avg `-0.0075` n `20`; unknown avg `8.3809` n `883`
- 24h: commodity avg `1.1529` n `12`; crypto_alt avg `3.0347` n `234`; crypto_major avg `1.3184` n `8`; equity avg `-0.2352` n `141`; fx avg `0.0181` n `6`; index avg `-0.0384` n `26`; metal avg `-0.0419` n `20`; unknown avg `266.8862` n `833`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
