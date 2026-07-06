# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T04:07:32.332835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.0039` n `229`; crypto_major avg `0.0638` n `8`; equity avg `-0.0249` n `88`; fx avg `-0.0001` n `6`; index avg `-0.015` n `25`; metal avg `-0.0114` n `20`; unknown avg `-0.1262` n `765`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.2495` n `229`; crypto_major avg `-0.3664` n `8`; equity avg `0.1086` n `88`; fx avg `-0.0058` n `6`; index avg `-0.033` n `25`; metal avg `-0.06` n `20`; unknown avg `12.4364` n `765`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.4767` n `229`; crypto_major avg `-0.5052` n `8`; equity avg `-1.0102` n `88`; fx avg `-0.0345` n `6`; index avg `-0.2876` n `25`; metal avg `-0.2406` n `20`; unknown avg `-0.3316` n `763`
- 24h: commodity avg `-0.2219` n `12`; crypto_alt avg `0.5465` n `229`; crypto_major avg `1.3338` n `8`; equity avg `-0.8728` n `88`; fx avg `0.0762` n `6`; index avg `-0.1361` n `25`; metal avg `-0.2459` n `20`; unknown avg `1.0981` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
