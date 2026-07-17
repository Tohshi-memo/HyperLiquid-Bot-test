# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T18:22:31.031276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.1346` n `230`; crypto_major avg `-0.2031` n `8`; equity avg `-0.3198` n `96`; fx avg `0.001` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0155` n `20`; unknown avg `-0.0178` n `769`
- 1h: commodity avg `0.055` n `12`; crypto_alt avg `-0.293` n `230`; crypto_major avg `-0.2986` n `8`; equity avg `-0.7552` n `96`; fx avg `0.0033` n `6`; index avg `-0.1011` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.0186` n `769`
- 4h: commodity avg `0.234` n `12`; crypto_alt avg `0.3548` n `230`; crypto_major avg `0.4374` n `8`; equity avg `0.4605` n `96`; fx avg `0.0743` n `6`; index avg `0.0754` n `25`; metal avg `0.1058` n `20`; unknown avg `0.2268` n `769`
- 24h: commodity avg `0.8803` n `12`; crypto_alt avg `-1.3054` n `230`; crypto_major avg `-1.5258` n `8`; equity avg `-1.3183` n `94`; fx avg `0.0968` n `6`; index avg `-0.2645` n `25`; metal avg `-0.1293` n `20`; unknown avg `-0.0566` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
