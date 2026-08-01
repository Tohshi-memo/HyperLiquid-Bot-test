# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T07:07:26.345683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.039` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `-0.0176` n `102`; fx avg `-0.007` n `6`; index avg `-0.0274` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0597` n `781`
- 1h: commodity avg `-0.0203` n `12`; crypto_alt avg `0.0557` n `230`; crypto_major avg `0.1143` n `8`; equity avg `0.0921` n `102`; fx avg `-0.0093` n `6`; index avg `0.0071` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0278` n `781`
- 4h: commodity avg `-0.095` n `12`; crypto_alt avg `0.0023` n `230`; crypto_major avg `-0.0826` n `8`; equity avg `-0.019` n `102`; fx avg `-0.0266` n `6`; index avg `-0.0337` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0736` n `765`
- 24h: commodity avg `0.8075` n `12`; crypto_alt avg `0.4097` n `230`; crypto_major avg `-1.4233` n `8`; equity avg `-2.1019` n `102`; fx avg `-0.0347` n `6`; index avg `-0.2572` n `25`; metal avg `-0.1706` n `20`; unknown avg `4.7218` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
