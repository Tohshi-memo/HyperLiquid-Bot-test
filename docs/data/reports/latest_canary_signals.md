# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T17:07:32.198381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.0539` n `230`; crypto_major avg `-0.0521` n `8`; equity avg `0.0801` n `114`; fx avg `-0.0041` n `6`; index avg `0.0051` n `25`; metal avg `-0.0257` n `20`; unknown avg `-0.109` n `791`
- 1h: commodity avg `0.0343` n `12`; crypto_alt avg `0.1699` n `230`; crypto_major avg `0.0125` n `8`; equity avg `0.0672` n `114`; fx avg `-0.0202` n `6`; index avg `0.0003` n `25`; metal avg `-0.0257` n `20`; unknown avg `18.6897` n `791`
- 4h: commodity avg `0.129` n `12`; crypto_alt avg `0.6121` n `230`; crypto_major avg `0.2929` n `8`; equity avg `-0.8484` n `114`; fx avg `0.0962` n `6`; index avg `-0.1721` n `25`; metal avg `0.0426` n `20`; unknown avg `-0.0172` n `786`
- 24h: commodity avg `0.0197` n `12`; crypto_alt avg `0.5172` n `230`; crypto_major avg `-0.411` n `8`; equity avg `-0.6494` n `114`; fx avg `0.0826` n `6`; index avg `-0.1283` n `25`; metal avg `0.0675` n `20`; unknown avg `0.4495` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
