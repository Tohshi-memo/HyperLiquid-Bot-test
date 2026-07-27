# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T22:22:31.335302+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0273` n `12`; crypto_alt avg `-0.0079` n `230`; crypto_major avg `-0.0206` n `8`; equity avg `-0.1015` n `102`; fx avg `-0.005` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0227` n `20`; unknown avg `-0.0134` n `774`
- 1h: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.4149` n `230`; crypto_major avg `-0.4218` n `8`; equity avg `-0.2857` n `102`; fx avg `-0.0029` n `6`; index avg `-0.0257` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0859` n `774`
- 4h: commodity avg `-0.0895` n `12`; crypto_alt avg `-0.0963` n `230`; crypto_major avg `-0.2274` n `8`; equity avg `0.6495` n `102`; fx avg `-0.0198` n `6`; index avg `0.1056` n `25`; metal avg `0.0467` n `20`; unknown avg `95.707` n `774`
- 24h: commodity avg `-0.5791` n `12`; crypto_alt avg `-1.9448` n `230`; crypto_major avg `-1.4562` n `8`; equity avg `-1.5924` n `102`; fx avg `-0.0455` n `6`; index avg `-0.4777` n `25`; metal avg `-0.013` n `20`; unknown avg `97.4337` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1931`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
