# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T01:07:25.048364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.0289` n `230`; crypto_major avg `-0.1138` n `8`; equity avg `0.1401` n `102`; fx avg `0.0074` n `6`; index avg `0.0375` n `25`; metal avg `0.0418` n `20`; unknown avg `-0.0545` n `784`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.2479` n `230`; crypto_major avg `-0.3141` n `8`; equity avg `0.5839` n `102`; fx avg `-0.223` n `6`; index avg `0.0033` n `25`; metal avg `-0.0528` n `20`; unknown avg `-0.0597` n `784`
- 4h: commodity avg `-0.093` n `12`; crypto_alt avg `-0.5156` n `230`; crypto_major avg `-0.5048` n `8`; equity avg `0.4327` n `102`; fx avg `-0.2642` n `6`; index avg `-0.0575` n `25`; metal avg `-0.1816` n `20`; unknown avg `1.4121` n `783`
- 24h: commodity avg `-0.9825` n `12`; crypto_alt avg `0.2947` n `230`; crypto_major avg `0.7788` n `8`; equity avg `1.6` n `102`; fx avg `-0.2877` n `6`; index avg `0.1991` n `25`; metal avg `0.0996` n `20`; unknown avg `1.5057` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
