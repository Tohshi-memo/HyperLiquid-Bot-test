# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T19:49:02.626405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0414` n `229`; crypto_major avg `-0.0403` n `8`; equity avg `-0.0318` n `92`; fx avg `0.0024` n `6`; index avg `-0.0029` n `25`; metal avg `0.0235` n `20`; unknown avg `0.1905` n `765`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.3279` n `229`; crypto_major avg `0.3979` n `8`; equity avg `0.0115` n `92`; fx avg `0.0034` n `6`; index avg `-0.0063` n `25`; metal avg `0.0443` n `20`; unknown avg `0.1509` n `765`
- 4h: commodity avg `0.332` n `12`; crypto_alt avg `0.2655` n `229`; crypto_major avg `0.235` n `8`; equity avg `0.3393` n `92`; fx avg `-0.0305` n `6`; index avg `0.0926` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.0548` n `765`
- 24h: commodity avg `-0.2336` n `12`; crypto_alt avg `0.6939` n `229`; crypto_major avg `0.9555` n `8`; equity avg `-0.4808` n `92`; fx avg `-0.1553` n `6`; index avg `0.0345` n `25`; metal avg `0.103` n `20`; unknown avg `-0.1448` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
