# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T19:37:26.843185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.0831` n `230`; crypto_major avg `0.1509` n `8`; equity avg `-0.0144` n `102`; fx avg `0.0043` n `6`; index avg `0.0004` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0995` n `774`
- 1h: commodity avg `-0.1242` n `12`; crypto_alt avg `0.2776` n `230`; crypto_major avg `0.4729` n `8`; equity avg `0.8927` n `102`; fx avg `-0.0007` n `6`; index avg `0.1515` n `25`; metal avg `0.1113` n `20`; unknown avg `1182.9793` n `774`
- 4h: commodity avg `-0.2075` n `12`; crypto_alt avg `0.543` n `230`; crypto_major avg `0.6555` n `8`; equity avg `1.2764` n `102`; fx avg `-0.0284` n `6`; index avg `0.2034` n `25`; metal avg `0.0781` n `20`; unknown avg `1182.8674` n `774`
- 24h: commodity avg `-0.9905` n `12`; crypto_alt avg `-1.0046` n `230`; crypto_major avg `-0.1367` n `8`; equity avg `-1.0832` n `102`; fx avg `-0.0225` n `6`; index avg `-0.3259` n `25`; metal avg `0.2264` n `20`; unknown avg `1209.0118` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
