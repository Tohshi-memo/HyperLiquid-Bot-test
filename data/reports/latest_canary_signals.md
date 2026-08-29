# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T06:37:28.701383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.1438` n `231`; crypto_major avg `0.1895` n `8`; equity avg `0.0111` n `127`; fx avg `-0.0005` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.0497` n `793`
- 1h: commodity avg `-0.028` n `12`; crypto_alt avg `-0.4812` n `231`; crypto_major avg `-0.4631` n `8`; equity avg `-0.0104` n `127`; fx avg `-0.0058` n `6`; index avg `-0.004` n `26`; metal avg `-0.008` n `20`; unknown avg `0.0791` n `761`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.1146` n `231`; crypto_major avg `-0.0494` n `8`; equity avg `0.0816` n `127`; fx avg `0.0032` n `6`; index avg `0.0255` n `26`; metal avg `0.0105` n `20`; unknown avg `0.0031` n `761`
- 24h: commodity avg `-0.13` n `12`; crypto_alt avg `-2.2699` n `231`; crypto_major avg `-2.8607` n `8`; equity avg `-1.5487` n `127`; fx avg `-0.034` n `6`; index avg `-0.1221` n `26`; metal avg `-0.3898` n `20`; unknown avg `-0.3841` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
