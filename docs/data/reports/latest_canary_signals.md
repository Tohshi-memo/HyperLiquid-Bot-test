# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T10:06:37.424891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1211` n `12`; crypto_alt avg `0.0489` n `230`; crypto_major avg `0.018` n `8`; equity avg `0.0659` n `107`; fx avg `-0.0127` n `6`; index avg `0.0172` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.0063` n `781`
- 1h: commodity avg `-0.1053` n `12`; crypto_alt avg `-0.0985` n `230`; crypto_major avg `0.0251` n `8`; equity avg `0.0662` n `107`; fx avg `-0.0101` n `6`; index avg `0.0545` n `25`; metal avg `0.0369` n `20`; unknown avg `0.0656` n `781`
- 4h: commodity avg `0.1007` n `12`; crypto_alt avg `-0.316` n `230`; crypto_major avg `-0.2283` n `8`; equity avg `0.0563` n `107`; fx avg `0.0453` n `6`; index avg `-0.0082` n `25`; metal avg `-0.02` n `20`; unknown avg `0.8871` n `781`
- 24h: commodity avg `0.343` n `12`; crypto_alt avg `0.8076` n `230`; crypto_major avg `0.914` n `8`; equity avg `3.4097` n `107`; fx avg `0.0943` n `6`; index avg `0.3562` n `25`; metal avg `0.1541` n `20`; unknown avg `1.06` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
