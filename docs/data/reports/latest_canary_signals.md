# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T22:37:30.793960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0774` n `12`; crypto_alt avg `-0.0287` n `230`; crypto_major avg `-0.0163` n `8`; equity avg `-0.0298` n `92`; fx avg `-0.0008` n `6`; index avg `0.0015` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.0647` n `765`
- 1h: commodity avg `-0.215` n `12`; crypto_alt avg `-0.7026` n `230`; crypto_major avg `-0.6539` n `8`; equity avg `-0.3315` n `92`; fx avg `-0.018` n `6`; index avg `-0.0754` n `25`; metal avg `-0.2209` n `20`; unknown avg `0.1672` n `765`
- 4h: commodity avg `-0.186` n `12`; crypto_alt avg `-0.9242` n `230`; crypto_major avg `-0.981` n `8`; equity avg `-0.3037` n `92`; fx avg `-0.0494` n `6`; index avg `-0.0655` n `25`; metal avg `-0.2268` n `20`; unknown avg `0.1637` n `765`
- 24h: commodity avg `0.2242` n `12`; crypto_alt avg `-1.8373` n `230`; crypto_major avg `-1.3254` n `8`; equity avg `-0.5255` n `92`; fx avg `-0.0608` n `6`; index avg `-0.1667` n `25`; metal avg `-0.3211` n `20`; unknown avg `0.2752` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
