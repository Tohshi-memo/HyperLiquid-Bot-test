# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T20:44:46.973319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.2009` n `230`; crypto_major avg `0.1691` n `8`; equity avg `0.0328` n `121`; fx avg `-0.0039` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0408` n `793`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `0.983` n `230`; crypto_major avg `0.7394` n `8`; equity avg `0.0587` n `121`; fx avg `-0.0092` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0259` n `20`; unknown avg `-0.2568` n `793`
- 4h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.1386` n `230`; crypto_major avg `0.1117` n `8`; equity avg `-0.003` n `121`; fx avg `0.006` n `6`; index avg `-0.0364` n `25`; metal avg `-0.0748` n `20`; unknown avg `-0.431` n `793`
- 24h: commodity avg `0.1261` n `12`; crypto_alt avg `7.2606` n `230`; crypto_major avg `5.0684` n `8`; equity avg `1.0131` n `121`; fx avg `-0.0931` n `6`; index avg `0.1019` n `25`; metal avg `0.5177` n `20`; unknown avg `1.0785` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
