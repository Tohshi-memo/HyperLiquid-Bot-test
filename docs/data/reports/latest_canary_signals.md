# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T22:07:15.599598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.004` n `228`; crypto_major avg `0.011` n `8`; equity avg `0.0806` n `65`; fx avg `0.0` n `5`; index avg `0.0119` n `23`; metal avg `0.0129` n `18`; unknown avg `-0.0178` n `376`
- 1h: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.0094` n `228`; crypto_major avg `-0.0172` n `8`; equity avg `0.0429` n `65`; fx avg `-0.0289` n `5`; index avg `0.0497` n `23`; metal avg `0.0737` n `18`; unknown avg `0.2764` n `376`
- 4h: commodity avg `0.0143` n `12`; crypto_alt avg `0.015` n `228`; crypto_major avg `0.0058` n `8`; equity avg `0.3649` n `65`; fx avg `-0.0117` n `5`; index avg `0.0971` n `23`; metal avg `0.1921` n `18`; unknown avg `0.1806` n `376`
- 24h: commodity avg `0.3122` n `12`; crypto_alt avg `-0.0728` n `228`; crypto_major avg `0.1483` n `8`; equity avg `0.7202` n `65`; fx avg `-0.031` n `5`; index avg `0.3797` n `23`; metal avg `0.1424` n `18`; unknown avg `0.3459` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
