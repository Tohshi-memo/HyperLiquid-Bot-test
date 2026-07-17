# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T00:37:29.297894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.3342` n `230`; crypto_major avg `-0.3025` n `8`; equity avg `-0.3492` n `94`; fx avg `-0.0033` n `6`; index avg `-0.04` n `25`; metal avg `-0.0607` n `20`; unknown avg `-0.0661` n `768`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.2631` n `230`; crypto_major avg `-0.1551` n `8`; equity avg `-0.5758` n `94`; fx avg `0.0062` n `6`; index avg `-0.1177` n `25`; metal avg `-0.06` n `20`; unknown avg `-0.107` n `768`
- 4h: commodity avg `0.053` n `12`; crypto_alt avg `-1.1519` n `230`; crypto_major avg `-1.0803` n `8`; equity avg `-1.275` n `94`; fx avg `0.0175` n `6`; index avg `-0.1663` n `25`; metal avg `-0.0596` n `20`; unknown avg `-0.2478` n `768`
- 24h: commodity avg `-0.1484` n `12`; crypto_alt avg `-1.937` n `230`; crypto_major avg `-2.6854` n `8`; equity avg `-4.5973` n `94`; fx avg `-0.1406` n `6`; index avg `-0.6028` n `25`; metal avg `-0.8849` n `20`; unknown avg `-0.6689` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
