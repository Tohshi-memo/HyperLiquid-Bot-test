# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T04:52:17.026869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.1033` n `228`; crypto_major avg `-0.0411` n `8`; equity avg `-0.0319` n `67`; fx avg `0.008` n `6`; index avg `0.045` n `23`; metal avg `-0.0229` n `18`; unknown avg `0.0462` n `407`
- 1h: commodity avg `0.1302` n `12`; crypto_alt avg `0.5094` n `228`; crypto_major avg `0.2138` n `8`; equity avg `0.0169` n `67`; fx avg `-0.0021` n `6`; index avg `0.0726` n `23`; metal avg `-0.2945` n `18`; unknown avg `-0.2395` n `407`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `0.2921` n `228`; crypto_major avg `0.2726` n `8`; equity avg `-0.0668` n `67`; fx avg `-0.0941` n `6`; index avg `0.0731` n `23`; metal avg `-0.5104` n `18`; unknown avg `-0.5853` n `407`
- 24h: commodity avg `0.6201` n `12`; crypto_alt avg `-0.4805` n `228`; crypto_major avg `-1.2834` n `8`; equity avg `-0.5059` n `67`; fx avg `-0.012` n `6`; index avg `0.0364` n `23`; metal avg `-0.562` n `18`; unknown avg `0.278` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
