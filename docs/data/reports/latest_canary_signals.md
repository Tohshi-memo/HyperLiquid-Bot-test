# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T17:52:29.064456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6441` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1127` n `12`; crypto_alt avg `-0.2133` n `231`; crypto_major avg `0.0479` n `8`; equity avg `0.0219` n `127`; fx avg `0.0105` n `6`; index avg `-0.0295` n `26`; metal avg `0.0156` n `20`; unknown avg `0.875` n `792`
- 1h: commodity avg `0.1418` n `12`; crypto_alt avg `-0.2551` n `231`; crypto_major avg `-0.1804` n `8`; equity avg `0.0922` n `127`; fx avg `0.0023` n `6`; index avg `-0.0327` n `26`; metal avg `0.0257` n `20`; unknown avg `0.6028` n `792`
- 4h: commodity avg `0.1137` n `12`; crypto_alt avg `1.1283` n `231`; crypto_major avg `1.7402` n `8`; equity avg `0.0961` n `127`; fx avg `-0.0255` n `6`; index avg `0.0231` n `26`; metal avg `0.3805` n `20`; unknown avg `0.3121` n `792`
- 24h: commodity avg `0.331` n `12`; crypto_alt avg `3.8062` n `231`; crypto_major avg `4.4634` n `8`; equity avg `1.701` n `127`; fx avg `-0.0534` n `6`; index avg `0.1792` n `26`; metal avg `0.224` n `20`; unknown avg `0.9065` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
