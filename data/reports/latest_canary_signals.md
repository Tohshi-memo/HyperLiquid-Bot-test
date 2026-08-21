# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:22:24.747399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7421` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6224` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0628` n `12`; crypto_alt avg `0.2623` n `230`; crypto_major avg `0.4321` n `8`; equity avg `-0.2295` n `121`; fx avg `-0.0023` n `6`; index avg `-0.0574` n `25`; metal avg `0.0989` n `20`; unknown avg `0.1702` n `793`
- 1h: commodity avg `0.0636` n `12`; crypto_alt avg `1.1816` n `230`; crypto_major avg `0.7585` n `8`; equity avg `-0.2642` n `121`; fx avg `-0.0377` n `6`; index avg `-0.057` n `25`; metal avg `0.1351` n `20`; unknown avg `0.0518` n `793`
- 4h: commodity avg `0.0784` n `12`; crypto_alt avg `2.7269` n `230`; crypto_major avg `1.9675` n `8`; equity avg `0.3451` n `121`; fx avg `-0.0103` n `6`; index avg `0.0152` n `25`; metal avg `0.2254` n `20`; unknown avg `0.1102` n `777`
- 24h: commodity avg `0.2179` n `12`; crypto_alt avg `6.9393` n `230`; crypto_major avg `7.1606` n `8`; equity avg `0.0525` n `121`; fx avg `-0.0693` n `6`; index avg `-0.0406` n `25`; metal avg `0.7966` n `20`; unknown avg `2.3501` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1991`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
