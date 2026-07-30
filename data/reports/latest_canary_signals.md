# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T12:52:26.510259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.2124` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0331` n `12`; crypto_alt avg `-0.1019` n `230`; crypto_major avg `-0.12` n `8`; equity avg `0.2964` n `102`; fx avg `-0.0184` n `6`; index avg `0.041` n `25`; metal avg `-0.0538` n `20`; unknown avg `-0.0422` n `779`
- 1h: commodity avg `0.0414` n `12`; crypto_alt avg `-0.0507` n `230`; crypto_major avg `-0.0698` n `8`; equity avg `0.8563` n `102`; fx avg `-0.0001` n `6`; index avg `0.0929` n `25`; metal avg `-0.076` n `20`; unknown avg `-0.0106` n `779`
- 4h: commodity avg `-0.2901` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `0.3004` n `8`; equity avg `2.5128` n `102`; fx avg `-0.0718` n `6`; index avg `0.3467` n `25`; metal avg `0.1541` n `20`; unknown avg `0.0324` n `771`
- 24h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.2298` n `230`; crypto_major avg `0.2991` n `8`; equity avg `-0.7784` n `102`; fx avg `-0.0673` n `6`; index avg `-0.0914` n `25`; metal avg `0.5061` n `20`; unknown avg `-0.2211` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
