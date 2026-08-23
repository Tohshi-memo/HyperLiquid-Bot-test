# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T07:43:49.184015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `-0.0322` n `230`; crypto_major avg `-0.1738` n `8`; equity avg `0.0116` n `121`; fx avg `-0.1061` n `6`; index avg `0.0062` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.0253` n `794`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `0.4334` n `230`; crypto_major avg `0.0007` n `8`; equity avg `0.0309` n `121`; fx avg `0.027` n `6`; index avg `0.0019` n `25`; metal avg `0.017` n `20`; unknown avg `0.1217` n `794`
- 4h: commodity avg `0.0045` n `12`; crypto_alt avg `0.3462` n `230`; crypto_major avg `-0.6119` n `8`; equity avg `-0.1389` n `121`; fx avg `0.0537` n `6`; index avg `-0.0291` n `25`; metal avg `-0.0139` n `20`; unknown avg `0.4388` n `778`
- 24h: commodity avg `-0.0036` n `12`; crypto_alt avg `-3.922` n `230`; crypto_major avg `-2.7369` n `8`; equity avg `-0.0933` n `121`; fx avg `0.1615` n `6`; index avg `-0.0211` n `25`; metal avg `0.0513` n `20`; unknown avg `2.351` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
