# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T04:07:26.070119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0333` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `0.0242` n `8`; equity avg `-0.0944` n `102`; fx avg `-0.0028` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.0078` n `774`
- 1h: commodity avg `0.1831` n `12`; crypto_alt avg `0.0995` n `230`; crypto_major avg `0.2106` n `8`; equity avg `0.3415` n `102`; fx avg `0.0021` n `6`; index avg `0.0816` n `25`; metal avg `0.0402` n `20`; unknown avg `-0.0058` n `774`
- 4h: commodity avg `-0.068` n `12`; crypto_alt avg `-0.1633` n `230`; crypto_major avg `-0.3248` n `8`; equity avg `-1.2299` n `102`; fx avg `-0.0494` n `6`; index avg `-0.2245` n `25`; metal avg `-0.2057` n `20`; unknown avg `0.4833` n `774`
- 24h: commodity avg `-0.7512` n `12`; crypto_alt avg `-3.8971` n `230`; crypto_major avg `-3.3983` n `8`; equity avg `-3.1854` n `102`; fx avg `-0.1173` n `6`; index avg `-0.6684` n `25`; metal avg `-0.2716` n `20`; unknown avg `1161.8691` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
