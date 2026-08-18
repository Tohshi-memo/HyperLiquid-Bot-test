# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T06:29:31.008865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.4823` n `230`; crypto_major avg `0.394` n `8`; equity avg `0.33` n `114`; fx avg `0.017` n `6`; index avg `0.0779` n `25`; metal avg `0.1287` n `20`; unknown avg `0.1593` n `793`
- 1h: commodity avg `0.0209` n `12`; crypto_alt avg `0.3061` n `230`; crypto_major avg `0.2238` n `8`; equity avg `-0.0519` n `114`; fx avg `0.0179` n `6`; index avg `-0.0492` n `25`; metal avg `0.0874` n `20`; unknown avg `-0.0236` n `761`
- 4h: commodity avg `0.1007` n `12`; crypto_alt avg `-0.1608` n `230`; crypto_major avg `0.2504` n `8`; equity avg `-0.3914` n `114`; fx avg `0.0043` n `6`; index avg `-0.1729` n `25`; metal avg `0.0353` n `20`; unknown avg `-0.0665` n `761`
- 24h: commodity avg `0.8156` n `12`; crypto_alt avg `-0.9955` n `230`; crypto_major avg `0.2259` n `8`; equity avg `-1.4981` n `114`; fx avg `-0.0049` n `6`; index avg `-0.4161` n `25`; metal avg `-0.127` n `20`; unknown avg `-0.0177` n `760`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1849`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
