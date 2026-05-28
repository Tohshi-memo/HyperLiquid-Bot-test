# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T15:52:22.856782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5064` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.2295` n `12`; crypto_alt avg `-0.1023` n `228`; crypto_major avg `0.0756` n `8`; equity avg `-0.1259` n `67`; fx avg `0.0078` n `6`; index avg `-0.0963` n `23`; metal avg `0.051` n `18`; unknown avg `-0.0365` n `419`
- 1h: commodity avg `0.3357` n `12`; crypto_alt avg `0.0753` n `228`; crypto_major avg `0.3007` n `8`; equity avg `0.4274` n `67`; fx avg `0.0085` n `6`; index avg `0.6535` n `23`; metal avg `0.3907` n `18`; unknown avg `-0.0739` n `419`
- 4h: commodity avg `0.1927` n `12`; crypto_alt avg `0.0413` n `228`; crypto_major avg `0.406` n `8`; equity avg `1.9124` n `67`; fx avg `0.0604` n `6`; index avg `1.2534` n `23`; metal avg `1.8491` n `18`; unknown avg `-0.1492` n `419`
- 24h: commodity avg `0.7062` n `12`; crypto_alt avg `-5.8284` n `228`; crypto_major avg `-3.1118` n `8`; equity avg `1.3669` n `67`; fx avg `0.0086` n `6`; index avg `1.1463` n `23`; metal avg `0.4422` n `18`; unknown avg `-1.8487` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
