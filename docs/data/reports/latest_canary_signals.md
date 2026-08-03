# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T14:07:28.255335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0792` n `12`; crypto_alt avg `0.1059` n `230`; crypto_major avg `0.128` n `8`; equity avg `0.5283` n `102`; fx avg `0.0208` n `6`; index avg `0.0503` n `25`; metal avg `0.0399` n `20`; unknown avg `0.0087` n `785`
- 1h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.7519` n `230`; crypto_major avg `0.7339` n `8`; equity avg `0.7505` n `102`; fx avg `-0.0548` n `6`; index avg `-0.0295` n `25`; metal avg `0.0145` n `20`; unknown avg `0.1712` n `785`
- 4h: commodity avg `-0.1554` n `12`; crypto_alt avg `0.694` n `230`; crypto_major avg `0.5689` n `8`; equity avg `0.0016` n `102`; fx avg `-0.0591` n `6`; index avg `-0.1352` n `25`; metal avg `-0.3756` n `20`; unknown avg `0.3355` n `784`
- 24h: commodity avg `-0.3548` n `12`; crypto_alt avg `0.2094` n `230`; crypto_major avg `0.643` n `8`; equity avg `-0.0786` n `102`; fx avg `-0.2041` n `6`; index avg `-0.2121` n `25`; metal avg `-0.5255` n `20`; unknown avg `1.4417` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
