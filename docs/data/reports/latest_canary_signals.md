# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T21:52:22.262373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2105` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `-0.2399` n `228`; crypto_major avg `-0.2749` n `8`; equity avg `-0.0035` n `74`; fx avg `-0.0078` n `6`; index avg `0.134` n `23`; metal avg `-0.0903` n `18`; unknown avg `0.058` n `547`
- 1h: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.6375` n `228`; crypto_major avg `-0.7018` n `8`; equity avg `-0.4783` n `74`; fx avg `-0.0606` n `6`; index avg `-0.1052` n `23`; metal avg `-0.121` n `18`; unknown avg `-0.1328` n `547`
- 4h: commodity avg `0.2717` n `12`; crypto_alt avg `0.0302` n `228`; crypto_major avg `-0.2794` n `8`; equity avg `0.6413` n `74`; fx avg `-0.1363` n `6`; index avg `0.9311` n `23`; metal avg `0.1297` n `18`; unknown avg `0.1442` n `547`
- 24h: commodity avg `-0.8066` n `12`; crypto_alt avg `-2.6307` n `228`; crypto_major avg `-3.716` n `8`; equity avg `-2.1849` n `74`; fx avg `0.3441` n `6`; index avg `-1.0539` n `23`; metal avg `-1.6564` n `18`; unknown avg `-1.3045` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0417`, n `668`, weak_sample_signal
