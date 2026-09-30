# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T12:52:30.983942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.4118` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.406` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9874` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `0.468` n `234`; crypto_major avg `0.5853` n `8`; equity avg `0.1191` n `142`; fx avg `-0.0298` n `6`; index avg `0.0002` n `26`; metal avg `-0.0068` n `20`; unknown avg `2.6652` n `963`
- 1h: commodity avg `-0.1342` n `12`; crypto_alt avg `1.2362` n `234`; crypto_major avg `1.4069` n `8`; equity avg `0.6264` n `142`; fx avg `-0.0373` n `6`; index avg `0.1434` n `26`; metal avg `0.1692` n `20`; unknown avg `7.4105` n `955`
- 4h: commodity avg `0.0198` n `12`; crypto_alt avg `1.8127` n `234`; crypto_major avg `2.4316` n `8`; equity avg `0.4442` n `142`; fx avg `0.0247` n `6`; index avg `0.0621` n `26`; metal avg `0.0256` n `20`; unknown avg `7.5287` n `955`
- 24h: commodity avg `-0.0722` n `12`; crypto_alt avg `0.9657` n `234`; crypto_major avg `0.4796` n `8`; equity avg `0.3549` n `142`; fx avg `0.0322` n `6`; index avg `0.0998` n `26`; metal avg `0.2641` n `20`; unknown avg `2685.7872` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
