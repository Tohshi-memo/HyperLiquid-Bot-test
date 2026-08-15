# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T07:39:43.132435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0514` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `0.0161` n `8`; equity avg `-0.0051` n `114`; fx avg `0.0015` n `6`; index avg `-0.0036` n `25`; metal avg `-0.003` n `20`; unknown avg `0.0011` n `791`
- 1h: commodity avg `-0.1231` n `12`; crypto_alt avg `-0.068` n `230`; crypto_major avg `-0.0278` n `8`; equity avg `0.0662` n `114`; fx avg `-0.0047` n `6`; index avg `0.0172` n `25`; metal avg `0.0082` n `20`; unknown avg `0.0066` n `791`
- 4h: commodity avg `-0.1643` n `12`; crypto_alt avg `0.2267` n `230`; crypto_major avg `-0.1597` n `8`; equity avg `-0.0142` n `114`; fx avg `-0.029` n `6`; index avg `-0.016` n `25`; metal avg `-0.0074` n `20`; unknown avg `-0.0721` n `759`
- 24h: commodity avg `-0.2728` n `12`; crypto_alt avg `1.0134` n `230`; crypto_major avg `0.0735` n `8`; equity avg `-0.0687` n `114`; fx avg `0.1011` n `6`; index avg `-0.0593` n `25`; metal avg `0.2775` n `20`; unknown avg `-0.1297` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1771`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1472`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.142`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `669`, weak_sample_signal
