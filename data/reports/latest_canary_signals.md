# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T22:22:31.690337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.1374` n `233`; crypto_major avg `0.0712` n `8`; equity avg `0.032` n `136`; fx avg `-0.0026` n `6`; index avg `0.0099` n `26`; metal avg `-0.0009` n `20`; unknown avg `0.1118` n `784`
- 1h: commodity avg `0.0468` n `12`; crypto_alt avg `0.0136` n `233`; crypto_major avg `0.0366` n `8`; equity avg `-0.0342` n `136`; fx avg `0.0284` n `6`; index avg `-0.0019` n `26`; metal avg `-0.0354` n `20`; unknown avg `0.3583` n `762`
- 4h: commodity avg `0.2033` n `12`; crypto_alt avg `0.1664` n `233`; crypto_major avg `0.3038` n `8`; equity avg `-0.3219` n `136`; fx avg `0.0406` n `6`; index avg `0.0005` n `26`; metal avg `-0.118` n `20`; unknown avg `-0.0247` n `718`
- 24h: commodity avg `1.171` n `12`; crypto_alt avg `-1.0531` n `233`; crypto_major avg `-1.3932` n `8`; equity avg `-1.9092` n `136`; fx avg `0.1449` n `6`; index avg `-0.3226` n `26`; metal avg `-1.2646` n `20`; unknown avg `-0.7345` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
