# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T17:37:30.449564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.2226` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.1035` n `239`; crypto_major avg `-0.036` n `8`; equity avg `-0.052` n `160`; fx avg `-0.0006` n `6`; index avg `0.028` n `27`; metal avg `-0.0165` n `20`; unknown avg `0.7152` n `1261`
- 1h: commodity avg `0.0692` n `13`; crypto_alt avg `-0.515` n `239`; crypto_major avg `-0.3924` n `8`; equity avg `0.358` n `160`; fx avg `0.0024` n `6`; index avg `0.0726` n `27`; metal avg `-0.0485` n `20`; unknown avg `0.756` n `1255`
- 4h: commodity avg `0.1973` n `13`; crypto_alt avg `-0.0293` n `239`; crypto_major avg `0.3551` n `8`; equity avg `3.5777` n `160`; fx avg `0.0164` n `6`; index avg `0.3957` n `27`; metal avg `-0.0088` n `20`; unknown avg `5.6087` n `1249`
- 24h: commodity avg `-0.3006` n `13`; crypto_alt avg `0.7729` n `239`; crypto_major avg `-2.3621` n `8`; equity avg `4.0015` n `160`; fx avg `-0.1556` n `6`; index avg `0.467` n `27`; metal avg `0.3872` n `20`; unknown avg `7.5732` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
