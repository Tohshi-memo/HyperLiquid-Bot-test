# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T10:37:27.899327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0538` n `13`; crypto_alt avg `-0.0193` n `235`; crypto_major avg `-0.0326` n `8`; equity avg `-0.0031` n `150`; fx avg `0.003` n `6`; index avg `0.0034` n `26`; metal avg `0.0541` n `20`; unknown avg `-0.0274` n `1074`
- 1h: commodity avg `-0.0962` n `13`; crypto_alt avg `0.47` n `235`; crypto_major avg `0.2695` n `8`; equity avg `0.0777` n `150`; fx avg `0.0055` n `6`; index avg `0.0087` n `26`; metal avg `-0.0225` n `20`; unknown avg `-0.1432` n `1072`
- 4h: commodity avg `-0.3464` n `13`; crypto_alt avg `0.7206` n `235`; crypto_major avg `0.5124` n `8`; equity avg `0.2115` n `149`; fx avg `0.0397` n `6`; index avg `0.0361` n `26`; metal avg `0.1037` n `20`; unknown avg `-0.0052` n `992`
- 24h: commodity avg `-0.8274` n `13`; crypto_alt avg `-0.3493` n `235`; crypto_major avg `-0.2568` n `8`; equity avg `0.6622` n `149`; fx avg `0.0245` n `6`; index avg `0.2483` n `26`; metal avg `-0.0446` n `20`; unknown avg `0.1603` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
