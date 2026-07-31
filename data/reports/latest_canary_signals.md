# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T04:34:53.668211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `12`; crypto_alt avg `0.1401` n `230`; crypto_major avg `0.137` n `8`; equity avg `0.1533` n `102`; fx avg `0.0219` n `6`; index avg `0.0569` n `25`; metal avg `0.0425` n `20`; unknown avg `-0.2234` n `779`
- 1h: commodity avg `-0.0527` n `12`; crypto_alt avg `-0.0268` n `230`; crypto_major avg `-0.0281` n `8`; equity avg `0.403` n `102`; fx avg `0.0431` n `6`; index avg `0.0672` n `25`; metal avg `0.046` n `20`; unknown avg `-0.0836` n `779`
- 4h: commodity avg `-0.3532` n `12`; crypto_alt avg `-0.3655` n `230`; crypto_major avg `-0.5993` n `8`; equity avg `0.0275` n `102`; fx avg `0.127` n `6`; index avg `-0.0004` n `25`; metal avg `-0.1408` n `20`; unknown avg `0.2041` n `779`
- 24h: commodity avg `-0.2305` n `12`; crypto_alt avg `0.077` n `230`; crypto_major avg `0.8467` n `8`; equity avg `8.6489` n `102`; fx avg `-0.0458` n `6`; index avg `1.1431` n `25`; metal avg `0.6039` n `20`; unknown avg `0.0688` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
