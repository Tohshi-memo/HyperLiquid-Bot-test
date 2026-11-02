# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T06:07:28.272122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0599` n `13`; crypto_alt avg `-0.219` n `238`; crypto_major avg `-0.1295` n `8`; equity avg `-0.0271` n `156`; fx avg `-0.0027` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0618` n `20`; unknown avg `0.2187` n `1240`
- 1h: commodity avg `0.0893` n `13`; crypto_alt avg `-0.3852` n `238`; crypto_major avg `-0.1417` n `8`; equity avg `0.1273` n `156`; fx avg `-0.0233` n `6`; index avg `0.0175` n `27`; metal avg `0.0982` n `20`; unknown avg `1.4252` n `1235`
- 4h: commodity avg `-0.1532` n `13`; crypto_alt avg `-0.4508` n `238`; crypto_major avg `-0.1022` n `8`; equity avg `0.7455` n `156`; fx avg `0.0516` n `6`; index avg `0.1144` n `27`; metal avg `0.0431` n `20`; unknown avg `1.6885` n `1179`
- 24h: commodity avg `-0.346` n `13`; crypto_alt avg `-1.4303` n `238`; crypto_major avg `0.041` n `8`; equity avg `1.2961` n `156`; fx avg `0.1783` n `6`; index avg `0.3509` n `27`; metal avg `0.1805` n `20`; unknown avg `3.1416` n `1068`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
