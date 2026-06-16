# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T05:37:32.650636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `0.0739` n `228`; crypto_major avg `0.0239` n `8`; equity avg `-0.0844` n `77`; fx avg `-0.0068` n `6`; index avg `0.1444` n `23`; metal avg `-0.2282` n `18`; unknown avg `0.0598` n `687`
- 1h: commodity avg `-0.0757` n `12`; crypto_alt avg `0.5642` n `228`; crypto_major avg `0.6319` n `8`; equity avg `0.0336` n `77`; fx avg `-0.0281` n `6`; index avg `0.0721` n `23`; metal avg `-0.1393` n `18`; unknown avg `-0.173` n `687`
- 4h: commodity avg `-0.3719` n `12`; crypto_alt avg `0.0543` n `228`; crypto_major avg `0.2509` n `8`; equity avg `0.397` n `77`; fx avg `-0.0256` n `6`; index avg `0.0415` n `23`; metal avg `0.1227` n `18`; unknown avg `-0.1682` n `679`
- 24h: commodity avg `0.2004` n `12`; crypto_alt avg `0.1338` n `228`; crypto_major avg `2.3085` n `8`; equity avg `1.229` n `76`; fx avg `-0.0917` n `6`; index avg `0.5802` n `23`; metal avg `-0.4254` n `18`; unknown avg `0.9463` n `503`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
