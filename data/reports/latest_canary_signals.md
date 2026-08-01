# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T15:07:36.757080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.021` n `230`; crypto_major avg `0.0322` n `8`; equity avg `-0.0226` n `102`; fx avg `-0.0143` n `6`; index avg `-0.0176` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0326` n `782`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.0262` n `230`; crypto_major avg `0.0366` n `8`; equity avg `-0.0044` n `102`; fx avg `-0.0179` n `6`; index avg `0.0029` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.0052` n `782`
- 4h: commodity avg `0.0262` n `12`; crypto_alt avg `0.1887` n `230`; crypto_major avg `0.2042` n `8`; equity avg `-0.1025` n `102`; fx avg `-0.0408` n `6`; index avg `-0.0328` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.1109` n `781`
- 24h: commodity avg `0.3828` n `12`; crypto_alt avg `0.4463` n `230`; crypto_major avg `-0.3459` n `8`; equity avg `-0.8318` n `102`; fx avg `-0.0541` n `6`; index avg `-0.0425` n `25`; metal avg `0.0427` n `20`; unknown avg `4.2379` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
