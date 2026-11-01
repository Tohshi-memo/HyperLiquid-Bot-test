# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T14:52:26.795288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `0.0699` n `238`; crypto_major avg `0.044` n `8`; equity avg `-0.0159` n `156`; fx avg `0.0176` n `6`; index avg `0.0035` n `27`; metal avg `0.0004` n `20`; unknown avg `0.2552` n `1263`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `0.0058` n `238`; crypto_major avg `0.1619` n `8`; equity avg `-0.0374` n `156`; fx avg `0.0255` n `6`; index avg `0.0081` n `27`; metal avg `-0.0068` n `20`; unknown avg `1.5654` n `1257`
- 4h: commodity avg `0.0239` n `13`; crypto_alt avg `0.1453` n `238`; crypto_major avg `-0.023` n `8`; equity avg `-0.0173` n `156`; fx avg `0.0129` n `6`; index avg `0.0329` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.1521` n `1251`
- 24h: commodity avg `0.0775` n `13`; crypto_alt avg `0.5216` n `238`; crypto_major avg `0.5858` n `8`; equity avg `0.4287` n `156`; fx avg `-0.0099` n `6`; index avg `0.0668` n `27`; metal avg `0.0547` n `20`; unknown avg `1.6961` n `1018`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
