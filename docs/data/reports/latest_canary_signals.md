# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T09:52:27.860460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `-0.1189` n `230`; crypto_major avg `-0.0947` n `8`; equity avg `-0.0248` n `102`; fx avg `0.0067` n `6`; index avg `0.0337` n `25`; metal avg `0.0124` n `20`; unknown avg `0.0127` n `781`
- 1h: commodity avg `-0.0449` n `12`; crypto_alt avg `-0.1975` n `230`; crypto_major avg `-0.1539` n `8`; equity avg `-0.0813` n `102`; fx avg `0.0028` n `6`; index avg `0.0328` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0101` n `781`
- 4h: commodity avg `0.007` n `12`; crypto_alt avg `-0.1373` n `230`; crypto_major avg `-0.0464` n `8`; equity avg `0.0164` n `102`; fx avg `0.0127` n `6`; index avg `0.0597` n `25`; metal avg `0.0193` n `20`; unknown avg `0.0174` n `765`
- 24h: commodity avg `0.5366` n `12`; crypto_alt avg `0.2904` n `230`; crypto_major avg `-1.0803` n `8`; equity avg `-2.5819` n `102`; fx avg `-0.0377` n `6`; index avg `-0.2453` n `25`; metal avg `-0.0335` n `20`; unknown avg `4.8331` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1076`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1051`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.104`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0888`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0733`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0676`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0661`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0648`, n `669`, weak_sample_signal
