# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T11:37:29.329253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `12`; crypto_alt avg `0.1493` n `230`; crypto_major avg `0.0513` n `8`; equity avg `0.0026` n `92`; fx avg `-0.0102` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0167` n `765`
- 1h: commodity avg `-0.0281` n `12`; crypto_alt avg `0.0884` n `230`; crypto_major avg `0.1263` n `8`; equity avg `0.0123` n `92`; fx avg `-0.0021` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.1468` n `765`
- 4h: commodity avg `0.0134` n `12`; crypto_alt avg `0.2948` n `230`; crypto_major avg `0.221` n `8`; equity avg `0.043` n `92`; fx avg `-0.0052` n `6`; index avg `0.0046` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.209` n `761`
- 24h: commodity avg `-0.3226` n `12`; crypto_alt avg `0.1979` n `229`; crypto_major avg `-0.4219` n `8`; equity avg `-0.3364` n `92`; fx avg `-0.1072` n `6`; index avg `0.1154` n `25`; metal avg `0.2003` n `20`; unknown avg `2.78` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
