# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T19:07:31.350625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0479` n `12`; crypto_alt avg `-0.3267` n `230`; crypto_major avg `-0.5004` n `8`; equity avg `-0.2523` n `102`; fx avg `0.0089` n `6`; index avg `-0.0824` n `25`; metal avg `-0.0281` n `20`; unknown avg `0.075` n `778`
- 1h: commodity avg `-0.0525` n `12`; crypto_alt avg `-0.2192` n `230`; crypto_major avg `-0.2368` n `8`; equity avg `0.4609` n `102`; fx avg `0.0197` n `6`; index avg `0.0961` n `25`; metal avg `0.2017` n `20`; unknown avg `-0.38` n `778`
- 4h: commodity avg `-0.0852` n `12`; crypto_alt avg `0.5642` n `230`; crypto_major avg `0.4081` n `8`; equity avg `1.4435` n `102`; fx avg `0.0093` n `6`; index avg `0.3101` n `25`; metal avg `0.7617` n `20`; unknown avg `-0.1228` n `778`
- 24h: commodity avg `1.2779` n `12`; crypto_alt avg `-1.4311` n `230`; crypto_major avg `0.3114` n `8`; equity avg `-0.2975` n `102`; fx avg `-0.037` n `6`; index avg `-0.1045` n `25`; metal avg `0.53` n `20`; unknown avg `-0.6392` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
