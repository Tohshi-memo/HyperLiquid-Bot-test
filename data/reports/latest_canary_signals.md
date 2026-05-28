# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T07:52:22.523363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1218` n `12`; crypto_alt avg `-0.2442` n `228`; crypto_major avg `-0.1635` n `8`; equity avg `-0.0606` n `67`; fx avg `-0.0109` n `6`; index avg `-0.0212` n `23`; metal avg `-0.0114` n `18`; unknown avg `-0.0748` n `419`
- 1h: commodity avg `0.2423` n `12`; crypto_alt avg `0.3412` n `228`; crypto_major avg `0.3865` n `8`; equity avg `0.1765` n `67`; fx avg `0.0126` n `6`; index avg `-0.0163` n `23`; metal avg `0.0636` n `18`; unknown avg `0.6295` n `419`
- 4h: commodity avg `-0.2682` n `12`; crypto_alt avg `-0.6428` n `228`; crypto_major avg `0.2981` n `8`; equity avg `0.9029` n `67`; fx avg `-0.004` n `6`; index avg `0.2489` n `23`; metal avg `0.6099` n `18`; unknown avg `0.3803` n `409`
- 24h: commodity avg `0.2934` n `12`; crypto_alt avg `-4.6913` n `228`; crypto_major avg `-3.4145` n `8`; equity avg `-1.1924` n `67`; fx avg `-0.1219` n `6`; index avg `-0.8527` n `23`; metal avg `-1.143` n `18`; unknown avg `-1.4083` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1695`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
