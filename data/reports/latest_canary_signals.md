# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T06:52:28.410412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0901` n `12`; crypto_alt avg `-0.018` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `-0.143` n `102`; fx avg `-0.0069` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.0049` n `784`
- 1h: commodity avg `-0.174` n `12`; crypto_alt avg `-0.2704` n `230`; crypto_major avg `-0.263` n `8`; equity avg `-0.2123` n `102`; fx avg `0.0515` n `6`; index avg `-0.0138` n `25`; metal avg `0.0371` n `20`; unknown avg `-0.034` n `768`
- 4h: commodity avg `-0.2175` n `12`; crypto_alt avg `-0.2831` n `230`; crypto_major avg `-0.4408` n `8`; equity avg `-0.3523` n `102`; fx avg `0.059` n `6`; index avg `-0.0427` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0222` n `768`
- 24h: commodity avg `-0.3843` n `12`; crypto_alt avg `-0.9786` n `230`; crypto_major avg `-0.7519` n `8`; equity avg `0.603` n `102`; fx avg `-0.1752` n `6`; index avg `-0.0192` n `25`; metal avg `-0.0474` n `20`; unknown avg `0.9515` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
