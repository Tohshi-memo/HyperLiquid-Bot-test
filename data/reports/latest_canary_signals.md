# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T08:07:27.769254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `12`; crypto_alt avg `0.2197` n `234`; crypto_major avg `0.0758` n `8`; equity avg `0.0186` n `140`; fx avg `-0.0005` n `6`; index avg `-0.0021` n `26`; metal avg `0.0175` n `20`; unknown avg `0.5312` n `935`
- 1h: commodity avg `0.0634` n `12`; crypto_alt avg `-0.137` n `234`; crypto_major avg `-0.0668` n `8`; equity avg `0.0073` n `140`; fx avg `0.0048` n `6`; index avg `-0.0049` n `26`; metal avg `0.0087` n `20`; unknown avg `0.6034` n `935`
- 4h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.3618` n `234`; crypto_major avg `-0.1136` n `8`; equity avg `-0.0415` n `140`; fx avg `0.003` n `6`; index avg `-0.0254` n `26`; metal avg `0.0139` n `20`; unknown avg `8.8362` n `895`
- 24h: commodity avg `0.2426` n `12`; crypto_alt avg `-0.4475` n `234`; crypto_major avg `-1.7839` n `8`; equity avg `-0.1973` n `140`; fx avg `-0.0566` n `6`; index avg `-0.0406` n `26`; metal avg `0.0203` n `20`; unknown avg `0.6625` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
