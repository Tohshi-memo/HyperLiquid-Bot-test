# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T00:07:31.884303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0925` n `12`; crypto_alt avg `-0.0129` n `230`; crypto_major avg `-0.0969` n `8`; equity avg `-0.0057` n `92`; fx avg `0.0001` n `6`; index avg `-0.1088` n `25`; metal avg `-0.0798` n `20`; unknown avg `-0.12` n `766`
- 1h: commodity avg `0.1774` n `12`; crypto_alt avg `0.4406` n `230`; crypto_major avg `0.4968` n `8`; equity avg `-0.1985` n `92`; fx avg `0.0282` n `6`; index avg `-0.1453` n `25`; metal avg `-0.0931` n `20`; unknown avg `0.08` n `766`
- 4h: commodity avg `0.3933` n `12`; crypto_alt avg `-0.317` n `230`; crypto_major avg `-0.1012` n `8`; equity avg `-0.646` n `92`; fx avg `-0.0081` n `6`; index avg `-0.2521` n `25`; metal avg `-0.1275` n `20`; unknown avg `-0.3464` n `766`
- 24h: commodity avg `1.1938` n `12`; crypto_alt avg `-2.4081` n `230`; crypto_major avg `-2.9243` n `8`; equity avg `-3.7888` n `92`; fx avg `-0.0578` n `6`; index avg `-0.8541` n `25`; metal avg `-0.5637` n `20`; unknown avg `-0.4688` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
