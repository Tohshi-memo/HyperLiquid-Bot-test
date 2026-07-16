# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T07:37:30.040154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `-0.3506` n `230`; crypto_major avg `-0.5405` n `8`; equity avg `-0.2024` n `94`; fx avg `0.0202` n `6`; index avg `-0.0274` n `25`; metal avg `-0.0373` n `20`; unknown avg `-0.0765` n `768`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `-0.3449` n `230`; crypto_major avg `-0.4348` n `8`; equity avg `-0.2664` n `94`; fx avg `-0.025` n `6`; index avg `-0.0267` n `25`; metal avg `-0.0302` n `20`; unknown avg `-0.0435` n `768`
- 4h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.5593` n `230`; crypto_major avg `-0.4273` n `8`; equity avg `-0.5794` n `94`; fx avg `-0.0493` n `6`; index avg `-0.0684` n `25`; metal avg `-0.1732` n `20`; unknown avg `0.0671` n `752`
- 24h: commodity avg `-0.1975` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `-0.064` n `8`; equity avg `-2.6027` n `93`; fx avg `0.0642` n `6`; index avg `-0.4515` n `25`; metal avg `-0.0292` n `20`; unknown avg `-0.1273` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
