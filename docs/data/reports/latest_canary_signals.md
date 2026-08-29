# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T18:07:28.243155+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.0642` n `231`; crypto_major avg `0.0007` n `8`; equity avg `0.0015` n `128`; fx avg `-0.0029` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.0435` n `792`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-0.3036` n `231`; crypto_major avg `-0.1142` n `8`; equity avg `-0.0012` n `128`; fx avg `0.0102` n `6`; index avg `-0.0033` n `26`; metal avg `0.0086` n `20`; unknown avg `-0.0156` n `792`
- 4h: commodity avg `-0.0085` n `12`; crypto_alt avg `0.115` n `231`; crypto_major avg `0.5283` n `8`; equity avg `0.0332` n `128`; fx avg `0.0106` n `6`; index avg `0.0098` n `26`; metal avg `0.0586` n `20`; unknown avg `0.128` n `778`
- 24h: commodity avg `0.0818` n `12`; crypto_alt avg `0.4963` n `231`; crypto_major avg `0.6365` n `8`; equity avg `0.1045` n `128`; fx avg `-0.0305` n `6`; index avg `0.0074` n `26`; metal avg `0.0849` n `20`; unknown avg `0.0587` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2246`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
