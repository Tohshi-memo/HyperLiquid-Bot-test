# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T21:22:29.845388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `12`; crypto_alt avg `0.0019` n `230`; crypto_major avg `0.0561` n `8`; equity avg `0.0262` n `102`; fx avg `0.0339` n `6`; index avg `0.0178` n `25`; metal avg `0.04` n `20`; unknown avg `-0.0004` n `783`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `0.1514` n `230`; crypto_major avg `0.1618` n `8`; equity avg `0.0378` n `102`; fx avg `0.0733` n `6`; index avg `0.0101` n `25`; metal avg `0.0492` n `20`; unknown avg `0.0227` n `783`
- 4h: commodity avg `0.0342` n `12`; crypto_alt avg `0.2233` n `230`; crypto_major avg `0.5546` n `8`; equity avg `0.1867` n `102`; fx avg `0.1567` n `6`; index avg `0.0358` n `25`; metal avg `0.1214` n `20`; unknown avg `0.057` n `782`
- 24h: commodity avg `-1.2415` n `12`; crypto_alt avg `1.3595` n `230`; crypto_major avg `1.8943` n `8`; equity avg `1.6893` n `102`; fx avg `0.0057` n `6`; index avg `0.3522` n `25`; metal avg `0.3803` n `20`; unknown avg `1.6327` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
