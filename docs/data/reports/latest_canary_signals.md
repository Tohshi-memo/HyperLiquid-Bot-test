# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T15:22:37.428762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-3.2579` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `0.0256` n `230`; crypto_major avg `0.2082` n `8`; equity avg `0.0103` n `102`; fx avg `0.0197` n `6`; index avg `0.0267` n `25`; metal avg `0.0421` n `20`; unknown avg `-0.0379` n `779`
- 1h: commodity avg `0.2107` n `12`; crypto_alt avg `-0.1596` n `230`; crypto_major avg `0.2045` n `8`; equity avg `-0.5204` n `102`; fx avg `0.0696` n `6`; index avg `-0.0704` n `25`; metal avg `0.0415` n `20`; unknown avg `-0.0678` n `779`
- 4h: commodity avg `0.2273` n `12`; crypto_alt avg `0.4195` n `230`; crypto_major avg `0.711` n `8`; equity avg `3.9689` n `102`; fx avg `-0.2528` n `6`; index avg `0.4365` n `25`; metal avg `0.116` n `20`; unknown avg `0.035` n `779`
- 24h: commodity avg `-0.0324` n `12`; crypto_alt avg `0.8894` n `230`; crypto_major avg `1.1907` n `8`; equity avg `4.2351` n `102`; fx avg `-0.3157` n `6`; index avg `0.432` n `25`; metal avg `0.7395` n `20`; unknown avg `-0.0896` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
