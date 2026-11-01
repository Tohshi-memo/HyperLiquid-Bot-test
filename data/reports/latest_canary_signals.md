# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T09:37:27.010797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `13`; crypto_alt avg `-0.0835` n `238`; crypto_major avg `-0.1005` n `8`; equity avg `-0.0293` n `156`; fx avg `0.0` n `6`; index avg `-0.0056` n `27`; metal avg `-0.002` n `20`; unknown avg `-0.0542` n `1263`
- 1h: commodity avg `0.002` n `13`; crypto_alt avg `-0.2595` n `238`; crypto_major avg `-0.0873` n `8`; equity avg `0.0497` n `156`; fx avg `-0.0088` n `6`; index avg `0.0055` n `27`; metal avg `-0.0036` n `20`; unknown avg `0.0174` n `1257`
- 4h: commodity avg `-0.0225` n `13`; crypto_alt avg `-0.0653` n `238`; crypto_major avg `0.0386` n `8`; equity avg `0.2203` n `156`; fx avg `-0.0051` n `6`; index avg `0.027` n `27`; metal avg `0.0175` n `20`; unknown avg `1.0816` n `1224`
- 24h: commodity avg `0.0093` n `13`; crypto_alt avg `0.5042` n `238`; crypto_major avg `0.5246` n `8`; equity avg `0.4665` n `156`; fx avg `-0.0164` n `6`; index avg `0.0259` n `27`; metal avg `0.0564` n `20`; unknown avg `2.4733` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
