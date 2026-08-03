# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T17:22:25.579958+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.668` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `0.0412` n `230`; crypto_major avg `0.0545` n `8`; equity avg `0.2716` n `103`; fx avg `0.0046` n `6`; index avg `0.0476` n `25`; metal avg `0.0177` n `20`; unknown avg `0.0383` n `784`
- 1h: commodity avg `0.027` n `12`; crypto_alt avg `0.0581` n `230`; crypto_major avg `-0.1251` n `8`; equity avg `0.1162` n `103`; fx avg `0.0041` n `6`; index avg `0.032` n `25`; metal avg `0.036` n `20`; unknown avg `0.0482` n `784`
- 4h: commodity avg `0.0786` n `12`; crypto_alt avg `0.6391` n `230`; crypto_major avg `1.1282` n `8`; equity avg `2.7962` n `103`; fx avg `-0.0077` n `6`; index avg `0.2351` n `25`; metal avg `0.1822` n `20`; unknown avg `-0.0688` n `784`
- 24h: commodity avg `-0.1259` n `12`; crypto_alt avg `0.3467` n `230`; crypto_major avg `0.9153` n `8`; equity avg `1.5733` n `102`; fx avg `-0.1661` n `6`; index avg `0.0123` n `25`; metal avg `-0.4673` n `20`; unknown avg `0.158` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
