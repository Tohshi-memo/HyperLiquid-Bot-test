# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T08:37:37.387326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1247` n `12`; crypto_alt avg `-0.2087` n `228`; crypto_major avg `-0.307` n `8`; equity avg `0.0303` n `79`; fx avg `0.0034` n `6`; index avg `-0.0019` n `23`; metal avg `0.0114` n `18`; unknown avg `-0.0042` n `701`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.3424` n `228`; crypto_major avg `-0.3196` n `8`; equity avg `-0.1096` n `79`; fx avg `-0.0151` n `6`; index avg `-0.0175` n `23`; metal avg `-0.1045` n `18`; unknown avg `-0.0899` n `693`
- 4h: commodity avg `0.0881` n `12`; crypto_alt avg `0.1625` n `228`; crypto_major avg `0.5133` n `8`; equity avg `0.4379` n `79`; fx avg `0.0042` n `6`; index avg `0.084` n `23`; metal avg `0.2413` n `18`; unknown avg `0.1034` n `661`
- 24h: commodity avg `-0.1677` n `12`; crypto_alt avg `0.0428` n `228`; crypto_major avg `0.2716` n `8`; equity avg `-0.2694` n `79`; fx avg `0.0147` n `6`; index avg `0.0089` n `23`; metal avg `0.3131` n `18`; unknown avg `0.0455` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
