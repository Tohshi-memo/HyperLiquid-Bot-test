# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-29T00:22:33.673124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0835` n `13`; crypto_alt avg `-0.235` n `239`; crypto_major avg `-0.1634` n `8`; equity avg `-0.0322` n `168`; fx avg `-0.0103` n `6`; index avg `-0.0009` n `27`; metal avg `-0.014` n `20`; unknown avg `-0.3238` n `1264`
- 1h: commodity avg `0.1323` n `13`; crypto_alt avg `-0.1918` n `239`; crypto_major avg `-0.2867` n `8`; equity avg `-0.0225` n `168`; fx avg `-0.0123` n `6`; index avg `-0.0004` n `27`; metal avg `0.0013` n `20`; unknown avg `201.1251` n `1252`
- 4h: commodity avg `0.261` n `13`; crypto_alt avg `-0.1595` n `239`; crypto_major avg `-0.0078` n `8`; equity avg `0.0667` n `168`; fx avg `0.0027` n `6`; index avg `0.0111` n `27`; metal avg `0.0016` n `20`; unknown avg `1.3784` n `1172`
- 24h: commodity avg `0.2229` n `13`; crypto_alt avg `-3.471` n `239`; crypto_major avg `-1.2019` n `8`; equity avg `-0.0706` n `168`; fx avg `0.0034` n `6`; index avg `-0.028` n `27`; metal avg `0.0224` n `20`; unknown avg `0.5805` n `1067`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
