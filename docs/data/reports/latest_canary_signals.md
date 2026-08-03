# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T12:07:34.431203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.0725` n `230`; crypto_major avg `-0.2254` n `8`; equity avg `-0.1602` n `102`; fx avg `0.0098` n `6`; index avg `-0.0332` n `25`; metal avg `-0.0802` n `20`; unknown avg `-0.0378` n `785`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.0446` n `230`; crypto_major avg `-0.1577` n `8`; equity avg `-0.4421` n `102`; fx avg `-0.001` n `6`; index avg `-0.0945` n `25`; metal avg `-0.0243` n `20`; unknown avg `-0.0027` n `785`
- 4h: commodity avg `-0.1658` n `12`; crypto_alt avg `0.1265` n `230`; crypto_major avg `0.0295` n `8`; equity avg `-1.434` n `102`; fx avg `-0.004` n `6`; index avg `-0.2136` n `25`; metal avg `-0.1695` n `20`; unknown avg `0.1878` n `784`
- 24h: commodity avg `-0.4999` n `12`; crypto_alt avg `-0.777` n `230`; crypto_major avg `-0.2766` n `8`; equity avg `-1.0277` n `102`; fx avg `-0.2` n `6`; index avg `-0.2231` n `25`; metal avg `-0.2282` n `20`; unknown avg `1.2754` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
