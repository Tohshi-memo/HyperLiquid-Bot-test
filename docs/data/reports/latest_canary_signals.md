# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T23:52:28.453159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `0.0078` n `230`; crypto_major avg `-0.0484` n `8`; equity avg `0.0601` n `102`; fx avg `-0.0241` n `6`; index avg `0.0165` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.0137` n `784`
- 1h: commodity avg `-0.112` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `0.1617` n `102`; fx avg `0.0163` n `6`; index avg `0.059` n `25`; metal avg `-0.0146` n `20`; unknown avg `-0.0688` n `783`
- 4h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.1398` n `230`; crypto_major avg `-0.0561` n `8`; equity avg `0.2958` n `102`; fx avg `0.0518` n `6`; index avg `0.0571` n `25`; metal avg `-0.1157` n `20`; unknown avg `1.6711` n `783`
- 24h: commodity avg `-1.0784` n `12`; crypto_alt avg `1.2061` n `230`; crypto_major avg `1.6508` n `8`; equity avg `1.7224` n `102`; fx avg `0.0618` n `6`; index avg `0.3531` n `25`; metal avg `0.189` n `20`; unknown avg `1.6021` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
