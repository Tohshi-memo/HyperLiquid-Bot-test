# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T02:07:13.602133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `-0.2227` n `228`; crypto_major avg `-0.2331` n `8`; equity avg `-0.3111` n `66`; fx avg `0.0031` n `6`; index avg `-0.1733` n `23`; metal avg `-0.38` n `18`; unknown avg `0.176` n `383`
- 1h: commodity avg `-0.0911` n `12`; crypto_alt avg `-0.5499` n `228`; crypto_major avg `-0.7533` n `8`; equity avg `-0.5202` n `66`; fx avg `0.0053` n `6`; index avg `-0.2567` n `23`; metal avg `-0.5481` n `18`; unknown avg `-0.1958` n `383`
- 4h: commodity avg `0.1591` n `12`; crypto_alt avg `-0.3508` n `228`; crypto_major avg `-0.5495` n `8`; equity avg `-0.6638` n `66`; fx avg `0.129` n `6`; index avg `-0.4794` n `23`; metal avg `-0.61` n `18`; unknown avg `-0.4416` n `383`
- 24h: commodity avg `-0.0279` n `12`; crypto_alt avg `0.4519` n `228`; crypto_major avg `-0.3977` n `8`; equity avg `-0.872` n `66`; fx avg `0.2164` n `6`; index avg `-0.2679` n `23`; metal avg `1.175` n `18`; unknown avg `0.1556` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
