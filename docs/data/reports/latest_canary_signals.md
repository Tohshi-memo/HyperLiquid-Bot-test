# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T10:22:32.362561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0849` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.0371` n `8`; equity avg `-0.0652` n `102`; fx avg `-0.0004` n `6`; index avg `-0.0081` n `25`; metal avg `-0.0134` n `20`; unknown avg `0.0021` n `774`
- 1h: commodity avg `0.0769` n `12`; crypto_alt avg `0.0406` n `230`; crypto_major avg `-0.1988` n `8`; equity avg `-0.3425` n `102`; fx avg `-0.0449` n `6`; index avg `-0.0593` n `25`; metal avg `-0.2237` n `20`; unknown avg `0.0242` n `774`
- 4h: commodity avg `-0.2032` n `12`; crypto_alt avg `-0.0994` n `230`; crypto_major avg `-0.1314` n `8`; equity avg `0.0241` n `102`; fx avg `-0.0485` n `6`; index avg `-0.0116` n `25`; metal avg `-0.2141` n `20`; unknown avg `-0.0145` n `774`
- 24h: commodity avg `-0.4273` n `12`; crypto_alt avg `-3.6348` n `230`; crypto_major avg `-3.8239` n `8`; equity avg `-4.3975` n `102`; fx avg `-0.1932` n `6`; index avg `-0.914` n `25`; metal avg `-0.6761` n `20`; unknown avg `998.0672` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
