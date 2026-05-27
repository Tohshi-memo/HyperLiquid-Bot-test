# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T19:37:24.428269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0687` n `12`; crypto_alt avg `0.1738` n `228`; crypto_major avg `0.1845` n `8`; equity avg `0.1139` n `67`; fx avg `0.0044` n `6`; index avg `-0.023` n `23`; metal avg `0.0194` n `18`; unknown avg `0.0444` n `419`
- 1h: commodity avg `0.1216` n `12`; crypto_alt avg `0.9497` n `228`; crypto_major avg `0.6102` n `8`; equity avg `0.1043` n `67`; fx avg `0.0175` n `6`; index avg `-0.0104` n `23`; metal avg `0.0429` n `18`; unknown avg `-0.0146` n `418`
- 4h: commodity avg `-0.4371` n `12`; crypto_alt avg `-0.8039` n `228`; crypto_major avg `-0.6693` n `8`; equity avg `0.4484` n `67`; fx avg `0.0272` n `6`; index avg `0.2512` n `23`; metal avg `0.1407` n `18`; unknown avg `-0.4353` n `418`
- 24h: commodity avg `-1.2117` n `12`; crypto_alt avg `0.0499` n `228`; crypto_major avg `-0.1904` n `8`; equity avg `-0.0133` n `67`; fx avg `-0.0644` n `6`; index avg `-0.4724` n `23`; metal avg `-1.1564` n `18`; unknown avg `-0.1919` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
