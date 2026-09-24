# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T17:24:55.816417+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2269` n `12`; crypto_alt avg `0.0027` n `234`; crypto_major avg `0.0391` n `8`; equity avg `-0.2245` n `141`; fx avg `-0.0044` n `6`; index avg `-0.0566` n `26`; metal avg `-0.0822` n `20`; unknown avg `0.3547` n `943`
- 1h: commodity avg `0.1975` n `12`; crypto_alt avg `-0.2052` n `234`; crypto_major avg `-0.2367` n `8`; equity avg `0.1335` n `141`; fx avg `-0.0081` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0798` n `20`; unknown avg `8.2516` n `941`
- 4h: commodity avg `0.787` n `12`; crypto_alt avg `2.3221` n `234`; crypto_major avg `1.4058` n `8`; equity avg `0.9452` n `141`; fx avg `0.0151` n `6`; index avg `0.0859` n `26`; metal avg `-0.0424` n `20`; unknown avg `7.603` n `883`
- 24h: commodity avg `1.2319` n `12`; crypto_alt avg `3.0147` n `234`; crypto_major avg `1.3347` n `8`; equity avg `-0.292` n `141`; fx avg `0.0146` n `6`; index avg `-0.0541` n `26`; metal avg `-0.0767` n `20`; unknown avg `266.5908` n `833`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
