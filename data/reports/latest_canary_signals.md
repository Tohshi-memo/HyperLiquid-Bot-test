# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T03:07:29.893635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0732` n `12`; crypto_alt avg `-0.019` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `-0.0247` n `102`; fx avg `0.0439` n `6`; index avg `-0.0037` n `25`; metal avg `-0.0023` n `20`; unknown avg `0.0698` n `781`
- 1h: commodity avg `0.0584` n `12`; crypto_alt avg `-0.0196` n `230`; crypto_major avg `-0.0308` n `8`; equity avg `-0.0187` n `102`; fx avg `0.0547` n `6`; index avg `0.0075` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.2835` n `781`
- 4h: commodity avg `-0.1191` n `12`; crypto_alt avg `0.6498` n `230`; crypto_major avg `0.1831` n `8`; equity avg `0.0723` n `102`; fx avg `0.0243` n `6`; index avg `0.044` n `25`; metal avg `-0.0277` n `20`; unknown avg `4.7876` n `781`
- 24h: commodity avg `0.9595` n `12`; crypto_alt avg `0.4835` n `230`; crypto_major avg `-1.2712` n `8`; equity avg `-1.9401` n `102`; fx avg `-0.1043` n `6`; index avg `-0.1684` n `25`; metal avg `-0.158` n `20`; unknown avg `4.9434` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
