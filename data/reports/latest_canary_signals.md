# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T06:37:30.181239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0612` n `12`; crypto_alt avg `0.1226` n `228`; crypto_major avg `0.1439` n `8`; equity avg `-0.0688` n `88`; fx avg `0.0092` n `6`; index avg `-0.0143` n `23`; metal avg `0.4303` n `20`; unknown avg `0.0532` n `765`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.3849` n `228`; crypto_major avg `0.2193` n `8`; equity avg `-0.095` n `88`; fx avg `0.0389` n `6`; index avg `-0.0284` n `23`; metal avg `0.6338` n `20`; unknown avg `-0.5038` n `739`
- 4h: commodity avg `-0.0528` n `12`; crypto_alt avg `0.1679` n `228`; crypto_major avg `-0.1951` n `8`; equity avg `0.1267` n `88`; fx avg `0.0144` n `6`; index avg `0.0667` n `23`; metal avg `0.8546` n `20`; unknown avg `7.8036` n `737`
- 24h: commodity avg `-0.3536` n `12`; crypto_alt avg `-0.1781` n `228`; crypto_major avg `0.7426` n `8`; equity avg `1.6365` n `88`; fx avg `0.1266` n `6`; index avg `0.184` n `23`; metal avg `-0.0813` n `20`; unknown avg `9.0407` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
