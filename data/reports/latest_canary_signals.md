# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T20:22:34.832492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0518` n `102`; fx avg `0.0077` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0243` n `20`; unknown avg `-0.0376` n `774`
- 1h: commodity avg `-0.0738` n `12`; crypto_alt avg `0.1277` n `230`; crypto_major avg `0.0015` n `8`; equity avg `0.0172` n `102`; fx avg `-0.0023` n `6`; index avg `-0.0122` n `25`; metal avg `-0.0457` n `20`; unknown avg `0.0072` n `774`
- 4h: commodity avg `-0.389` n `12`; crypto_alt avg `0.4506` n `230`; crypto_major avg `0.3426` n `8`; equity avg `0.9392` n `102`; fx avg `-0.0309` n `6`; index avg `0.1469` n `25`; metal avg `-0.0595` n `20`; unknown avg `95.8527` n `774`
- 24h: commodity avg `-1.0416` n `12`; crypto_alt avg `-0.8883` n `230`; crypto_major avg `-0.2502` n `8`; equity avg `-1.0294` n `102`; fx avg `-0.031` n `6`; index avg `-0.3364` n `25`; metal avg `0.2019` n `20`; unknown avg `97.7061` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
