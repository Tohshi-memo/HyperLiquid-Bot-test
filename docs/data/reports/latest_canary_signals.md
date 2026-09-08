# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T05:11:01.525536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0381` n `12`; crypto_alt avg `0.0385` n `232`; crypto_major avg `-0.108` n `8`; equity avg `-0.2897` n `134`; fx avg `-0.0238` n `6`; index avg `-0.0569` n `26`; metal avg `-0.0349` n `20`; unknown avg `3.3901` n `795`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `0.1701` n `232`; crypto_major avg `-0.0106` n `8`; equity avg `-0.3978` n `134`; fx avg `0.0073` n `6`; index avg `-0.0892` n `26`; metal avg `-0.0643` n `20`; unknown avg `1.5688` n `773`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `-0.3195` n `232`; crypto_major avg `-0.6033` n `8`; equity avg `-0.0582` n `134`; fx avg `-0.0387` n `6`; index avg `0.0049` n `26`; metal avg `0.0707` n `20`; unknown avg `0.1398` n `767`
- 24h: commodity avg `0.1064` n `12`; crypto_alt avg `0.5072` n `232`; crypto_major avg `-1.0609` n `8`; equity avg `0.3574` n `134`; fx avg `-0.2898` n `6`; index avg `0.1233` n `26`; metal avg `0.3639` n `20`; unknown avg `7463.0765` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
