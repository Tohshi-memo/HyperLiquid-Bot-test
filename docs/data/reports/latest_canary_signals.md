# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T14:22:31.614572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1472` n `12`; crypto_alt avg `-0.1774` n `233`; crypto_major avg `-0.1867` n `8`; equity avg `-0.4495` n `134`; fx avg `0.012` n `6`; index avg `-0.0958` n `26`; metal avg `-0.0982` n `20`; unknown avg `9.1718` n `797`
- 1h: commodity avg `0.0707` n `12`; crypto_alt avg `-0.68` n `233`; crypto_major avg `-0.7843` n `8`; equity avg `0.0656` n `134`; fx avg `0.0159` n `6`; index avg `0.0353` n `26`; metal avg `0.0242` n `20`; unknown avg `11.1166` n `773`
- 4h: commodity avg `0.0739` n `12`; crypto_alt avg `-0.1403` n `233`; crypto_major avg `-0.2013` n `8`; equity avg `0.265` n `134`; fx avg `0.0041` n `6`; index avg `0.0264` n `26`; metal avg `0.3429` n `20`; unknown avg `17.2734` n `766`
- 24h: commodity avg `0.3054` n `12`; crypto_alt avg `-0.0287` n `232`; crypto_major avg `0.7036` n `8`; equity avg `0.0936` n `134`; fx avg `-0.0912` n `6`; index avg `-0.0923` n `26`; metal avg `0.3226` n `20`; unknown avg `9.3281` n `685`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
