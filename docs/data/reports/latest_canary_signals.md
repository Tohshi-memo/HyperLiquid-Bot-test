# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T01:22:36.548931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.2398` n `234`; crypto_major avg `0.1934` n `8`; equity avg `0.0605` n `140`; fx avg `-0.032` n `6`; index avg `0.0032` n `26`; metal avg `-0.0391` n `20`; unknown avg `-0.0464` n `945`
- 1h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.0881` n `234`; crypto_major avg `0.2339` n `8`; equity avg `-0.078` n `140`; fx avg `0.0057` n `6`; index avg `-0.0343` n `26`; metal avg `-0.1524` n `20`; unknown avg `4.3314` n `943`
- 4h: commodity avg `0.0938` n `12`; crypto_alt avg `1.5483` n `234`; crypto_major avg `1.0915` n `8`; equity avg `0.0774` n `140`; fx avg `-0.0513` n `6`; index avg `-0.0381` n `26`; metal avg `-0.0907` n `20`; unknown avg `-0.1685` n `936`
- 24h: commodity avg `0.1` n `12`; crypto_alt avg `3.5766` n `234`; crypto_major avg `2.1592` n `8`; equity avg `0.6617` n `140`; fx avg `-0.2063` n `6`; index avg `0.042` n `26`; metal avg `0.1432` n `20`; unknown avg `1.3343` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
