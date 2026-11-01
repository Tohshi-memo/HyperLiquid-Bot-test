# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T16:37:33.550436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `13`; crypto_alt avg `-0.1475` n `238`; crypto_major avg `-0.0898` n `8`; equity avg `-0.0028` n `156`; fx avg `0.0112` n `6`; index avg `-0.0006` n `27`; metal avg `0.0012` n `20`; unknown avg `-0.0506` n `1263`
- 1h: commodity avg `-0.0815` n `13`; crypto_alt avg `-0.3157` n `238`; crypto_major avg `-0.1455` n `8`; equity avg `0.0281` n `156`; fx avg `0.0209` n `6`; index avg `0.0156` n `27`; metal avg `-0.0011` n `20`; unknown avg `-0.3482` n `1243`
- 4h: commodity avg `-0.0724` n `13`; crypto_alt avg `-0.1557` n `238`; crypto_major avg `0.0355` n `8`; equity avg `0.0634` n `156`; fx avg `0.029` n `6`; index avg `0.0655` n `27`; metal avg `0.0013` n `20`; unknown avg `-0.335` n `1245`
- 24h: commodity avg `0.0232` n `13`; crypto_alt avg `-0.7934` n `238`; crypto_major avg `0.0693` n `8`; equity avg `0.4982` n `156`; fx avg `0.0144` n `6`; index avg `0.0971` n `27`; metal avg `0.0385` n `20`; unknown avg `1.3015` n `1010`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
