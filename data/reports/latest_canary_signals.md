# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T15:07:32.015083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6221` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.5543` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0362` n `13`; crypto_alt avg `-0.1556` n `239`; crypto_major avg `-0.3315` n `8`; equity avg `-0.0601` n `160`; fx avg `0.0182` n `6`; index avg `0.0143` n `27`; metal avg `-0.0942` n `20`; unknown avg `0.9244` n `1257`
- 1h: commodity avg `0.0585` n `13`; crypto_alt avg `0.443` n `239`; crypto_major avg `0.6732` n `8`; equity avg `2.2275` n `160`; fx avg `0.0072` n `6`; index avg `0.2675` n `27`; metal avg `-0.0164` n `20`; unknown avg `1.7255` n `1255`
- 4h: commodity avg `-0.126` n `13`; crypto_alt avg `1.9385` n `239`; crypto_major avg `1.4259` n `8`; equity avg `3.048` n `160`; fx avg `-0.0097` n `6`; index avg `0.3509` n `27`; metal avg `0.0931` n `20`; unknown avg `23.76` n `1249`
- 24h: commodity avg `-0.4123` n `13`; crypto_alt avg `0.4064` n `239`; crypto_major avg `-2.6101` n `8`; equity avg `2.545` n `160`; fx avg `-0.1081` n `6`; index avg `0.3376` n `27`; metal avg `0.3757` n `20`; unknown avg `5.5706` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
