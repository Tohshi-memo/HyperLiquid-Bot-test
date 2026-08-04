# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T23:22:33.024337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0278` n `12`; crypto_alt avg `0.0272` n `230`; crypto_major avg `0.0481` n `8`; equity avg `0.0734` n `108`; fx avg `0.0021` n `6`; index avg `0.009` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.1312` n `781`
- 1h: commodity avg `-0.029` n `12`; crypto_alt avg `0.1669` n `230`; crypto_major avg `0.1771` n `8`; equity avg `0.1107` n `108`; fx avg `0.0075` n `6`; index avg `0.0244` n `25`; metal avg `-0.0629` n `20`; unknown avg `-0.0161` n `781`
- 4h: commodity avg `-0.1052` n `12`; crypto_alt avg `0.0997` n `230`; crypto_major avg `0.015` n `8`; equity avg `-0.432` n `108`; fx avg `0.0046` n `6`; index avg `-0.0536` n `25`; metal avg `-0.0985` n `20`; unknown avg `0.0092` n `781`
- 24h: commodity avg `-1.219` n `12`; crypto_alt avg `0.3277` n `230`; crypto_major avg `0.8669` n `8`; equity avg `3.0636` n `107`; fx avg `0.1088` n `6`; index avg `0.7102` n `25`; metal avg `0.8444` n `20`; unknown avg `0.4353` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
