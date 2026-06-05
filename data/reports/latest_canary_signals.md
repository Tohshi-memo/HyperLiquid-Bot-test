# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T21:07:26.536590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `1.9089` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.391` n `12`; crypto_alt avg `0.2173` n `228`; crypto_major avg `0.1978` n `8`; equity avg `-0.0433` n `74`; fx avg `-0.0172` n `6`; index avg `-0.0142` n `23`; metal avg `0.0155` n `18`; unknown avg `-0.0295` n `425`
- 1h: commodity avg `0.3627` n `12`; crypto_alt avg `2.245` n `228`; crypto_major avg `2.0759` n `8`; equity avg `0.167` n `74`; fx avg `-0.0068` n `6`; index avg `-0.1025` n `23`; metal avg `0.2909` n `18`; unknown avg `1.6172` n `425`
- 4h: commodity avg `0.3602` n `12`; crypto_alt avg `-0.2184` n `228`; crypto_major avg `-0.2699` n `8`; equity avg `-1.1476` n `74`; fx avg `-0.0518` n `6`; index avg `-1.5343` n `23`; metal avg `-0.8061` n `18`; unknown avg `-0.1765` n `424`
- 24h: commodity avg `-1.4569` n `12`; crypto_alt avg `-7.1177` n `228`; crypto_major avg `-5.9362` n `8`; equity avg `-6.4687` n `74`; fx avg `-0.0828` n `6`; index avg `-4.4932` n `23`; metal avg `-4.5215` n `18`; unknown avg `-1.9775` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
