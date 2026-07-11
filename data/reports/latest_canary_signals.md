# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T13:07:29.532715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0403` n `12`; crypto_alt avg `-0.0494` n `230`; crypto_major avg `-0.0113` n `8`; equity avg `-0.0433` n `92`; fx avg `-0.0011` n `6`; index avg `0.004` n `25`; metal avg `0.0076` n `20`; unknown avg `-0.0072` n `765`
- 1h: commodity avg `0.01` n `12`; crypto_alt avg `0.0841` n `230`; crypto_major avg `-0.0298` n `8`; equity avg `-0.0904` n `92`; fx avg `-0.0042` n `6`; index avg `-0.0027` n `25`; metal avg `0.0012` n `20`; unknown avg `0.0134` n `765`
- 4h: commodity avg `0.0512` n `12`; crypto_alt avg `0.157` n `230`; crypto_major avg `0.0223` n `8`; equity avg `-0.049` n `92`; fx avg `-0.0055` n `6`; index avg `0.0005` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.2167` n `761`
- 24h: commodity avg `-0.0505` n `12`; crypto_alt avg `0.4197` n `229`; crypto_major avg `-0.183` n `8`; equity avg `-0.2272` n `92`; fx avg `-0.0811` n `6`; index avg `0.1542` n `25`; metal avg `0.1053` n `20`; unknown avg `2.9434` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
