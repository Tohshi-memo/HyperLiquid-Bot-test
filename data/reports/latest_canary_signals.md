# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T10:52:36.025804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.0045` n `228`; crypto_major avg `0.0327` n `8`; equity avg `-0.03` n `77`; fx avg `-0.0016` n `6`; index avg `-0.0092` n `23`; metal avg `0.0705` n `18`; unknown avg `-0.0444` n `687`
- 1h: commodity avg `-0.2278` n `12`; crypto_alt avg `0.33` n `228`; crypto_major avg `0.4349` n `8`; equity avg `0.0761` n `77`; fx avg `0.0145` n `6`; index avg `0.0444` n `23`; metal avg `0.0487` n `18`; unknown avg `0.1659` n `687`
- 4h: commodity avg `-0.7851` n `12`; crypto_alt avg `1.0253` n `228`; crypto_major avg `1.032` n `8`; equity avg `0.4494` n `77`; fx avg `0.1042` n `6`; index avg `0.1653` n `23`; metal avg `0.9956` n `18`; unknown avg `0.264` n `687`
- 24h: commodity avg `0.0116` n `12`; crypto_alt avg `1.432` n `228`; crypto_major avg `3.2902` n `8`; equity avg `1.8147` n `76`; fx avg `-0.062` n `6`; index avg `0.4942` n `23`; metal avg `0.2366` n `18`; unknown avg `0.2145` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
