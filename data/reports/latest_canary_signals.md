# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T16:07:31.648663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.08` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.8189` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `-0.0261` n `228`; crypto_major avg `-0.2321` n `8`; equity avg `3.2293` n `77`; fx avg `0.0048` n `6`; index avg `0.0763` n `23`; metal avg `-0.125` n `18`; unknown avg `-0.1568` n `687`
- 1h: commodity avg `-0.2275` n `12`; crypto_alt avg `0.4282` n `228`; crypto_major avg `0.7877` n `8`; equity avg `0.6626` n `77`; fx avg `-0.0001` n `6`; index avg `0.286` n `23`; metal avg `-0.1078` n `18`; unknown avg `0.2418` n `687`
- 4h: commodity avg `0.1531` n `12`; crypto_alt avg `1.1514` n `228`; crypto_major avg `1.7054` n `8`; equity avg `1.2784` n `76`; fx avg `-0.0126` n `6`; index avg `0.4842` n `23`; metal avg `-0.1135` n `18`; unknown avg `0.5358` n `687`
- 24h: commodity avg `-1.0295` n `12`; crypto_alt avg `6.6325` n `228`; crypto_major avg `7.281` n `8`; equity avg `3.0226` n `76`; fx avg `0.0506` n `6`; index avg `1.3578` n `23`; metal avg `2.7077` n `18`; unknown avg `2.4444` n `527`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
