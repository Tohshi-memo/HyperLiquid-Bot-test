# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T22:14:30.210160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.186` n `12`; crypto_alt avg `0.0039` n `230`; crypto_major avg `0.1502` n `8`; equity avg `-0.0734` n `102`; fx avg `-0.0101` n `6`; index avg `-0.0298` n `25`; metal avg `-0.1376` n `20`; unknown avg `-0.0401` n `783`
- 1h: commodity avg `-0.3954` n `12`; crypto_alt avg `0.229` n `230`; crypto_major avg `0.4146` n `8`; equity avg `0.1033` n `102`; fx avg `0.0163` n `6`; index avg `0.0099` n `25`; metal avg `-0.0596` n `20`; unknown avg `1.4447` n `783`
- 4h: commodity avg `-0.3001` n `12`; crypto_alt avg `0.3731` n `230`; crypto_major avg `0.7827` n `8`; equity avg `0.3012` n `102`; fx avg `0.1268` n `6`; index avg `0.0328` n `25`; metal avg `0.0005` n `20`; unknown avg `2.6326` n `782`
- 24h: commodity avg `-1.373` n `12`; crypto_alt avg `1.3874` n `230`; crypto_major avg `2.0338` n `8`; equity avg `1.4513` n `102`; fx avg `-0.029` n `6`; index avg `0.3082` n `25`; metal avg `0.2528` n `20`; unknown avg `1.5822` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
