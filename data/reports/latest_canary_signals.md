# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T19:15:15.679517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.0692` n `238`; crypto_major avg `-0.0257` n `8`; equity avg `-0.0041` n `156`; fx avg `-0.0022` n `6`; index avg `0.0059` n `27`; metal avg `-0.0027` n `20`; unknown avg `-0.2915` n `1260`
- 1h: commodity avg `-0.0312` n `13`; crypto_alt avg `-0.0856` n `238`; crypto_major avg `-0.0248` n `8`; equity avg `0.0136` n `156`; fx avg `-0.009` n `6`; index avg `-0.0029` n `27`; metal avg `0.0026` n `20`; unknown avg `-0.272` n `1254`
- 4h: commodity avg `-0.0301` n `13`; crypto_alt avg `-0.1409` n `238`; crypto_major avg `0.3472` n `8`; equity avg `0.0727` n `156`; fx avg `-0.0227` n `6`; index avg `0.004` n `27`; metal avg `-0.0038` n `20`; unknown avg `0.341` n `1196`
- 24h: commodity avg `-0.3433` n `13`; crypto_alt avg `1.5468` n `238`; crypto_major avg `0.7942` n `8`; equity avg `1.0438` n `156`; fx avg `-0.0366` n `6`; index avg `0.0632` n `27`; metal avg `0.1386` n `20`; unknown avg `0.8593` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
