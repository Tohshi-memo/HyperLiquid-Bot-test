# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T05:52:31.340624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `12`; crypto_alt avg `0.0751` n `228`; crypto_major avg `0.0003` n `8`; equity avg `-0.0178` n `77`; fx avg `-0.0095` n `6`; index avg `0.0021` n `23`; metal avg `0.0779` n `18`; unknown avg `-0.2888` n `687`
- 1h: commodity avg `-0.0897` n `12`; crypto_alt avg `0.682` n `228`; crypto_major avg `0.6609` n `8`; equity avg `0.0737` n `77`; fx avg `-0.0034` n `6`; index avg `-0.0432` n `23`; metal avg `-0.1249` n `18`; unknown avg `-0.1472` n `687`
- 4h: commodity avg `-0.3193` n `12`; crypto_alt avg `0.0893` n `228`; crypto_major avg `0.2273` n `8`; equity avg `0.256` n `77`; fx avg `-0.0444` n `6`; index avg `0.026` n `23`; metal avg `0.1596` n `18`; unknown avg `-0.1144` n `679`
- 24h: commodity avg `0.1534` n `12`; crypto_alt avg `0.3898` n `228`; crypto_major avg `2.4213` n `8`; equity avg `1.2397` n `76`; fx avg `-0.091` n `6`; index avg `0.4667` n `23`; metal avg `-0.1654` n `18`; unknown avg `0.7609` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
