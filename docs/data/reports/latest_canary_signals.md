# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T08:37:28.502023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `-0.211` n `230`; crypto_major avg `-0.1431` n `8`; equity avg `-0.0956` n `96`; fx avg `0.0137` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0208` n `20`; unknown avg `-0.0219` n `768`
- 1h: commodity avg `-0.0212` n `12`; crypto_alt avg `-0.2778` n `230`; crypto_major avg `-0.0869` n `8`; equity avg `-0.6423` n `96`; fx avg `0.0363` n `6`; index avg `-0.1038` n `25`; metal avg `-0.0499` n `20`; unknown avg `-0.0323` n `768`
- 4h: commodity avg `-0.1365` n `12`; crypto_alt avg `-0.9411` n `230`; crypto_major avg `-0.9129` n `8`; equity avg `-1.028` n `96`; fx avg `0.0408` n `6`; index avg `-0.0932` n `25`; metal avg `-0.0849` n `20`; unknown avg `-0.1662` n `736`
- 24h: commodity avg `-0.1558` n `12`; crypto_alt avg `-2.1636` n `230`; crypto_major avg `-3.4085` n `8`; equity avg `-5.8667` n `94`; fx avg `-0.0266` n `6`; index avg `-0.8232` n `25`; metal avg `-0.8362` n `20`; unknown avg `-0.5711` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
