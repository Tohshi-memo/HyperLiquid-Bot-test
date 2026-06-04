# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T03:52:25.396486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.6785` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `0.1026` n `228`; crypto_major avg `0.2241` n `8`; equity avg `-0.1351` n `73`; fx avg `0.0046` n `6`; index avg `0.0118` n `23`; metal avg `-0.1056` n `18`; unknown avg `1.0189` n `420`
- 1h: commodity avg `0.1046` n `12`; crypto_alt avg `1.6934` n `228`; crypto_major avg `1.5126` n `8`; equity avg `0.2931` n `73`; fx avg `0.018` n `6`; index avg `0.1486` n `23`; metal avg `-0.1659` n `18`; unknown avg `1.4499` n `420`
- 4h: commodity avg `-0.3007` n `12`; crypto_alt avg `-1.9764` n `228`; crypto_major avg `-0.1021` n `8`; equity avg `0.5916` n `73`; fx avg `-0.0136` n `6`; index avg `0.1222` n `23`; metal avg `0.0213` n `18`; unknown avg `0.8101` n `419`
- 24h: commodity avg `0.105` n `12`; crypto_alt avg `0.2674` n `228`; crypto_major avg `-0.2192` n `8`; equity avg `-3.3706` n `73`; fx avg `-0.0017` n `6`; index avg `-1.1268` n `23`; metal avg `-1.8455` n `18`; unknown avg `0.7225` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
