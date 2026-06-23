# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T15:07:36.191887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0685` n `12`; crypto_alt avg `-0.3973` n `228`; crypto_major avg `-0.3942` n `8`; equity avg `-0.2157` n `86`; fx avg `0.0023` n `6`; index avg `-0.0133` n `23`; metal avg `0.0102` n `20`; unknown avg `-0.2004` n `764`
- 1h: commodity avg `0.1734` n `12`; crypto_alt avg `-0.4723` n `228`; crypto_major avg `-0.4419` n `8`; equity avg `-0.5884` n `86`; fx avg `-0.0331` n `6`; index avg `-0.0654` n `23`; metal avg `-0.0707` n `20`; unknown avg `-0.2288` n `764`
- 4h: commodity avg `-0.1565` n `12`; crypto_alt avg `0.2606` n `228`; crypto_major avg `-0.1512` n `8`; equity avg `0.7607` n `86`; fx avg `-0.0809` n `6`; index avg `0.045` n `23`; metal avg `0.0391` n `20`; unknown avg `-0.0482` n `764`
- 24h: commodity avg `-0.3586` n `12`; crypto_alt avg `-4.1446` n `228`; crypto_major avg `-4.6044` n `8`; equity avg `-3.2373` n `85`; fx avg `-0.1536` n `6`; index avg `-0.8905` n `23`; metal avg `-1.1395` n `20`; unknown avg `-0.1654` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
