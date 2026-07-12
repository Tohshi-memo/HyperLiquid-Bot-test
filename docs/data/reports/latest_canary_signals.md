# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T20:37:29.102524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0508` n `12`; crypto_alt avg `-0.0708` n `230`; crypto_major avg `-0.0648` n `8`; equity avg `-0.023` n `92`; fx avg `-0.0073` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0242` n `765`
- 1h: commodity avg `0.1118` n `12`; crypto_alt avg `-0.0663` n `230`; crypto_major avg `-0.0088` n `8`; equity avg `-0.0141` n `92`; fx avg `-0.0126` n `6`; index avg `-0.0048` n `25`; metal avg `-0.0044` n `20`; unknown avg `-0.0408` n `765`
- 4h: commodity avg `0.1433` n `12`; crypto_alt avg `-0.0846` n `230`; crypto_major avg `-0.0324` n `8`; equity avg `0.0631` n `92`; fx avg `-0.0311` n `6`; index avg `-0.0088` n `25`; metal avg `-0.007` n `20`; unknown avg `-0.1715` n `765`
- 24h: commodity avg `0.6314` n `12`; crypto_alt avg `-1.5931` n `230`; crypto_major avg `-0.6918` n `8`; equity avg `-0.1973` n `92`; fx avg `-0.0092` n `6`; index avg `-0.0894` n `25`; metal avg `-0.1126` n `20`; unknown avg `0.1879` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
