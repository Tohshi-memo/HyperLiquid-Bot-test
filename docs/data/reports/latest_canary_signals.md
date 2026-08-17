# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T11:22:28.507033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `-0.0611` n `8`; equity avg `-0.0813` n `114`; fx avg `0.0052` n `6`; index avg `-0.0094` n `25`; metal avg `0.0072` n `20`; unknown avg `0.01` n `792`
- 1h: commodity avg `-0.039` n `12`; crypto_alt avg `0.4131` n `230`; crypto_major avg `0.4291` n `8`; equity avg `0.0021` n `114`; fx avg `-0.0033` n `6`; index avg `0.0038` n `25`; metal avg `0.0383` n `20`; unknown avg `1.9952` n `792`
- 4h: commodity avg `0.2199` n `12`; crypto_alt avg `-0.0456` n `230`; crypto_major avg `0.0074` n `8`; equity avg `0.1037` n `114`; fx avg `0.0028` n `6`; index avg `0.0093` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0048` n `792`
- 24h: commodity avg `-0.0667` n `12`; crypto_alt avg `0.0563` n `230`; crypto_major avg `0.9519` n `8`; equity avg `1.2201` n `114`; fx avg `-0.026` n `6`; index avg `0.1444` n `25`; metal avg `0.209` n `20`; unknown avg `0.0497` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
