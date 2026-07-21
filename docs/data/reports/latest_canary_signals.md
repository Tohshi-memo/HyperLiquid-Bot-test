# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T16:22:26.091820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7659` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0433` n `12`; crypto_alt avg `-0.0737` n `230`; crypto_major avg `-0.0863` n `8`; equity avg `0.0823` n `98`; fx avg `0.0034` n `6`; index avg `0.0297` n `25`; metal avg `0.0487` n `20`; unknown avg `0.0688` n `771`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0733` n `230`; crypto_major avg `-0.1202` n `8`; equity avg `0.2036` n `98`; fx avg `-0.0077` n `6`; index avg `0.0396` n `25`; metal avg `0.0446` n `20`; unknown avg `0.0598` n `771`
- 4h: commodity avg `0.0022` n `12`; crypto_alt avg `-0.1846` n `230`; crypto_major avg `-0.2552` n `8`; equity avg `1.5107` n `98`; fx avg `-0.0194` n `6`; index avg `0.2371` n `25`; metal avg `0.1161` n `20`; unknown avg `0.2452` n `771`
- 24h: commodity avg `0.5742` n `12`; crypto_alt avg `0.9625` n `230`; crypto_major avg `0.8545` n `8`; equity avg `2.642` n `98`; fx avg `0.0013` n `6`; index avg `0.3689` n `25`; metal avg `0.6502` n `20`; unknown avg `0.3089` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0885`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0573`, n `666`, weak_sample_signal
