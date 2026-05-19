# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T10:07:18.122855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0686` n `12`; crypto_alt avg `0.0913` n `228`; crypto_major avg `0.1016` n `8`; equity avg `0.0745` n `66`; fx avg `-0.0065` n `6`; index avg `0.0583` n `23`; metal avg `0.0497` n `18`; unknown avg `-0.2143` n `383`
- 1h: commodity avg `-0.0903` n `12`; crypto_alt avg `-0.2508` n `228`; crypto_major avg `-0.4294` n `8`; equity avg `-0.3771` n `66`; fx avg `0.0252` n `6`; index avg `-0.295` n `23`; metal avg `0.173` n `18`; unknown avg `-0.2531` n `383`
- 4h: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.446` n `228`; crypto_major avg `-0.3187` n `8`; equity avg `-0.24` n `66`; fx avg `-0.063` n `6`; index avg `-0.2482` n `23`; metal avg `-0.2221` n `18`; unknown avg `-0.372` n `383`
- 24h: commodity avg `0.4545` n `12`; crypto_alt avg `1.6294` n `228`; crypto_major avg `0.8435` n `8`; equity avg `-1.6357` n `66`; fx avg `0.2348` n `6`; index avg `-0.7842` n `23`; metal avg `-0.1716` n `18`; unknown avg `0.774` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
