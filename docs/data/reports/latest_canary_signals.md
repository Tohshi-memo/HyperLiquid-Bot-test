# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T15:11:30.881137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.61` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `3.5992` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.5288` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.1567` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0601` n `12`; crypto_alt avg `0.0499` n `233`; crypto_major avg `-0.2285` n `8`; equity avg `-0.0255` n `136`; fx avg `0.0246` n `6`; index avg `0.02` n `26`; metal avg `-0.1409` n `20`; unknown avg `0.1005` n `794`
- 1h: commodity avg `0.0765` n `12`; crypto_alt avg `0.0575` n `233`; crypto_major avg `-0.6147` n `8`; equity avg `0.0854` n `136`; fx avg `0.0377` n `6`; index avg `0.0383` n `26`; metal avg `-0.2129` n `20`; unknown avg `1.8831` n `794`
- 4h: commodity avg `0.1807` n `12`; crypto_alt avg `4.0202` n `233`; crypto_major avg `3.7095` n `8`; equity avg `0.5528` n `136`; fx avg `0.0097` n `6`; index avg `0.1121` n `26`; metal avg `0.1103` n `20`; unknown avg `5.7064` n `772`
- 24h: commodity avg `-0.0408` n `12`; crypto_alt avg `2.0744` n `233`; crypto_major avg `2.668` n `8`; equity avg `-0.0564` n `136`; fx avg `-0.1113` n `6`; index avg `0.2024` n `26`; metal avg `0.0195` n `20`; unknown avg `5.3432` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
