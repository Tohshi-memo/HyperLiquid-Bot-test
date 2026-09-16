# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T11:22:30.590322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.0161` n `234`; crypto_major avg `0.0453` n `8`; equity avg `-0.0296` n `137`; fx avg `-0.0105` n `6`; index avg `-0.0234` n `27`; metal avg `-0.009` n `20`; unknown avg `-0.0241` n `919`
- 1h: commodity avg `-0.039` n `12`; crypto_alt avg `0.1686` n `234`; crypto_major avg `0.208` n `8`; equity avg `0.0912` n `137`; fx avg `-0.006` n `6`; index avg `0.0062` n `27`; metal avg `0.052` n `20`; unknown avg `0.1323` n `917`
- 4h: commodity avg `-0.0205` n `12`; crypto_alt avg `0.1638` n `234`; crypto_major avg `0.2445` n `8`; equity avg `0.0548` n `137`; fx avg `0.0111` n `6`; index avg `0.011` n `27`; metal avg `0.0275` n `20`; unknown avg `-0.1461` n `911`
- 24h: commodity avg `0.1893` n `12`; crypto_alt avg `-2.6012` n `234`; crypto_major avg `-2.5298` n `8`; equity avg `-0.3229` n `137`; fx avg `0.0984` n `6`; index avg `0.031` n `27`; metal avg `0.4651` n `20`; unknown avg `18889.6357` n `798`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
