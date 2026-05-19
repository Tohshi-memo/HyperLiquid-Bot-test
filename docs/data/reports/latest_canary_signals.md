# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T16:37:20.247595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `0.2878` n `228`; crypto_major avg `0.243` n `8`; equity avg `0.5022` n `66`; fx avg `-0.0028` n `6`; index avg `0.2274` n `23`; metal avg `0.1583` n `18`; unknown avg `0.0897` n `383`
- 1h: commodity avg `0.1908` n `12`; crypto_alt avg `0.2189` n `228`; crypto_major avg `0.1217` n `8`; equity avg `0.663` n `66`; fx avg `-0.0926` n `6`; index avg `0.4244` n `23`; metal avg `0.1179` n `18`; unknown avg `0.0525` n `383`
- 4h: commodity avg `0.3049` n `12`; crypto_alt avg `-0.1865` n `228`; crypto_major avg `0.03` n `8`; equity avg `0.655` n `66`; fx avg `-0.1033` n `6`; index avg `-0.0724` n `23`; metal avg `-1.1458` n `18`; unknown avg `-0.1297` n `383`
- 24h: commodity avg `0.694` n `12`; crypto_alt avg `0.725` n `228`; crypto_major avg `1.0078` n `8`; equity avg `0.5917` n `66`; fx avg `-0.0478` n `6`; index avg `-0.3601` n `23`; metal avg `-1.7635` n `18`; unknown avg `-0.2594` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
