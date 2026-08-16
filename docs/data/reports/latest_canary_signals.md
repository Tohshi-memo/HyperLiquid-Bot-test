# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T11:22:27.795283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.0162` n `230`; crypto_major avg `-0.0054` n `8`; equity avg `-0.0219` n `114`; fx avg `0.0055` n `6`; index avg `0.0011` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.0704` n `791`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `0.0426` n `230`; crypto_major avg `0.0498` n `8`; equity avg `-0.0345` n `114`; fx avg `0.0055` n `6`; index avg `0.0006` n `25`; metal avg `-0.0063` n `20`; unknown avg `-0.0137` n `791`
- 4h: commodity avg `0.0224` n `12`; crypto_alt avg `0.2322` n `230`; crypto_major avg `0.0197` n `8`; equity avg `-0.0391` n `114`; fx avg `0.0005` n `6`; index avg `-0.0079` n `25`; metal avg `0.0071` n `20`; unknown avg `0.0933` n `791`
- 24h: commodity avg `0.0678` n `12`; crypto_alt avg `0.0792` n `230`; crypto_major avg `0.1449` n `8`; equity avg `0.3218` n `114`; fx avg `0.0009` n `6`; index avg `0.0517` n `25`; metal avg `0.0173` n `20`; unknown avg `0.1847` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
