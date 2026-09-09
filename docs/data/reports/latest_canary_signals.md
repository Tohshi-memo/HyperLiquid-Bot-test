# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T11:07:29.829923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.2448` n `233`; crypto_major avg `-0.1633` n `8`; equity avg `0.0123` n `134`; fx avg `-0.0073` n `6`; index avg `0.0177` n `26`; metal avg `0.0226` n `20`; unknown avg `-0.1339` n `796`
- 1h: commodity avg `0.0177` n `12`; crypto_alt avg `-0.3555` n `233`; crypto_major avg `-0.2156` n `8`; equity avg `0.0013` n `134`; fx avg `-0.0015` n `6`; index avg `-0.0124` n `26`; metal avg `0.0646` n `20`; unknown avg `11.4297` n `796`
- 4h: commodity avg `0.1388` n `12`; crypto_alt avg `-1.0313` n `233`; crypto_major avg `-0.981` n `8`; equity avg `-0.7542` n `134`; fx avg `0.0248` n `6`; index avg `-0.1839` n `26`; metal avg `-0.0475` n `20`; unknown avg `0.3821` n `790`
- 24h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.5579` n `232`; crypto_major avg `0.6307` n `8`; equity avg `0.2915` n `134`; fx avg `-0.1063` n `6`; index avg `-0.1469` n `26`; metal avg `0.0346` n `20`; unknown avg `0.7825` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
