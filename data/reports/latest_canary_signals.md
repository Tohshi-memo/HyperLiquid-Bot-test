# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T11:30:41.632468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1458` n `12`; crypto_alt avg `0.0844` n `228`; crypto_major avg `0.0208` n `8`; equity avg `0.0033` n `66`; fx avg `0.0088` n `6`; index avg `0.0707` n `23`; metal avg `-0.0331` n `18`; unknown avg `0.0359` n `383`
- 1h: commodity avg `0.4116` n `12`; crypto_alt avg `-0.2895` n `228`; crypto_major avg `-0.2399` n `8`; equity avg `-0.1469` n `66`; fx avg `-0.0232` n `6`; index avg `0.0784` n `23`; metal avg `-0.0549` n `18`; unknown avg `-0.3605` n `383`
- 4h: commodity avg `0.2957` n `12`; crypto_alt avg `-1.0282` n `228`; crypto_major avg `-0.6279` n `8`; equity avg `-0.7778` n `66`; fx avg `-0.0716` n `6`; index avg `-0.3216` n `23`; metal avg `-0.1068` n `18`; unknown avg `-0.7054` n `383`
- 24h: commodity avg `1.1143` n `12`; crypto_alt avg `1.0975` n `228`; crypto_major avg `0.7419` n `8`; equity avg `-1.5194` n `66`; fx avg `0.1954` n `6`; index avg `-0.5401` n `23`; metal avg `-0.3066` n `18`; unknown avg `0.7484` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
