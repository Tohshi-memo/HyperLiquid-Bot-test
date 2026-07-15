# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T02:07:31.006821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `-0.0662` n `230`; crypto_major avg `0.055` n `8`; equity avg `0.3227` n `93`; fx avg `0.0007` n `6`; index avg `0.0824` n `25`; metal avg `0.0285` n `20`; unknown avg `-0.0912` n `767`
- 1h: commodity avg `0.0304` n `12`; crypto_alt avg `-0.0302` n `230`; crypto_major avg `-0.2104` n `8`; equity avg `0.6049` n `93`; fx avg `0.0194` n `6`; index avg `0.0926` n `25`; metal avg `-0.0755` n `20`; unknown avg `-0.1254` n `767`
- 4h: commodity avg `0.0332` n `12`; crypto_alt avg `0.2281` n `230`; crypto_major avg `-0.1572` n `8`; equity avg `0.9373` n `93`; fx avg `0.0443` n `6`; index avg `0.1617` n `25`; metal avg `-0.0117` n `20`; unknown avg `-0.4132` n `765`
- 24h: commodity avg `0.2523` n `12`; crypto_alt avg `1.6933` n `230`; crypto_major avg `2.677` n `8`; equity avg `2.2218` n `92`; fx avg `0.0705` n `6`; index avg `0.6208` n `25`; metal avg `0.5532` n `20`; unknown avg `0.1493` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
