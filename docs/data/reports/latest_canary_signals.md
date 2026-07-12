# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T09:52:29.539356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0962` n `230`; crypto_major avg `0.1093` n `8`; equity avg `0.0164` n `92`; fx avg `0.0027` n `6`; index avg `0.0055` n `25`; metal avg `0.0031` n `20`; unknown avg `-0.0541` n `765`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `0.0252` n `230`; crypto_major avg `0.0578` n `8`; equity avg `-0.0165` n `92`; fx avg `-0.0047` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0072` n `765`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `-0.1355` n `230`; crypto_major avg `0.0886` n `8`; equity avg `-0.0682` n `92`; fx avg `-0.0007` n `6`; index avg `-0.0012` n `25`; metal avg `-0.0185` n `20`; unknown avg `1.9684` n `747`
- 24h: commodity avg `0.5247` n `12`; crypto_alt avg `-0.7369` n `230`; crypto_major avg `-0.5019` n `8`; equity avg `-0.1979` n `92`; fx avg `-0.0039` n `6`; index avg `-0.1243` n `25`; metal avg `-0.1154` n `20`; unknown avg `-0.0661` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
