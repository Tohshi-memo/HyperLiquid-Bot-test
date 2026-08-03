# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T17:37:35.152521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5645` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0645` n `230`; crypto_major avg `0.0603` n `8`; equity avg `0.1751` n `103`; fx avg `-0.0047` n `6`; index avg `0.0344` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.067` n `784`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1838` n `230`; crypto_major avg `0.0904` n `8`; equity avg `0.4612` n `103`; fx avg `0.0021` n `6`; index avg `0.0873` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0478` n `784`
- 4h: commodity avg `0.1874` n `12`; crypto_alt avg `0.7883` n `230`; crypto_major avg `1.2707` n `8`; equity avg `2.8352` n `103`; fx avg `0.022` n `6`; index avg `0.2873` n `25`; metal avg `0.2029` n `20`; unknown avg `-0.0648` n `784`
- 24h: commodity avg `-0.0934` n `12`; crypto_alt avg `0.3564` n `230`; crypto_major avg `0.8468` n `8`; equity avg `1.8144` n `102`; fx avg `-0.1666` n `6`; index avg `0.045` n `25`; metal avg `-0.4585` n `20`; unknown avg `0.1258` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
