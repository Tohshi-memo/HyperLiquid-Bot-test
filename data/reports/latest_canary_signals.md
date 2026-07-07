# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T01:22:28.773215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0445` n `12`; crypto_alt avg `-0.1112` n `229`; crypto_major avg `-0.0632` n `8`; equity avg `-0.2701` n `91`; fx avg `0.0023` n `6`; index avg `-0.0325` n `25`; metal avg `-0.0715` n `20`; unknown avg `-0.1722` n `763`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.5122` n `229`; crypto_major avg `-0.2211` n `8`; equity avg `-0.5777` n `91`; fx avg `-0.0082` n `6`; index avg `-0.1631` n `25`; metal avg `-0.3051` n `20`; unknown avg `0.2654` n `763`
- 4h: commodity avg `0.0056` n `12`; crypto_alt avg `-0.8643` n `229`; crypto_major avg `-0.873` n `8`; equity avg `-1.1561` n `91`; fx avg `0.0109` n `6`; index avg `-0.3084` n `25`; metal avg `-0.396` n `20`; unknown avg `3.1252` n `763`
- 24h: commodity avg `0.2265` n `12`; crypto_alt avg `-0.0888` n `229`; crypto_major avg `-0.6952` n `8`; equity avg `-1.4933` n `90`; fx avg `0.1055` n `6`; index avg `-0.2941` n `25`; metal avg `-0.6052` n `20`; unknown avg `-0.3197` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
