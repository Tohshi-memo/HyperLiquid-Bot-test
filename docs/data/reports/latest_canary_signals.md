# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T11:52:29.653353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0495` n `12`; crypto_alt avg `-0.0484` n `230`; crypto_major avg `-0.0274` n `8`; equity avg `0.1642` n `114`; fx avg `0.0036` n `6`; index avg `0.019` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0034` n `795`
- 1h: commodity avg `0.1373` n `12`; crypto_alt avg `0.155` n `230`; crypto_major avg `0.2335` n `8`; equity avg `0.2728` n `114`; fx avg `-0.0016` n `6`; index avg `0.0321` n `25`; metal avg `-0.0335` n `20`; unknown avg `0.0237` n `795`
- 4h: commodity avg `0.0708` n `12`; crypto_alt avg `0.3151` n `230`; crypto_major avg `0.2178` n `8`; equity avg `-0.5615` n `114`; fx avg `-0.0257` n `6`; index avg `-0.0476` n `25`; metal avg `-0.0484` n `20`; unknown avg `-0.0075` n `795`
- 24h: commodity avg `0.6801` n `12`; crypto_alt avg `-0.8472` n `230`; crypto_major avg `0.1729` n `8`; equity avg `-2.2953` n `114`; fx avg `-0.0406` n `6`; index avg `-0.4977` n `25`; metal avg `-0.2223` n `20`; unknown avg `-0.0157` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
