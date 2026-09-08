# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T05:37:26.065554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `-0.0069` n `232`; crypto_major avg `-0.0184` n `8`; equity avg `-0.2843` n `134`; fx avg `0.0311` n `6`; index avg `-0.0666` n `26`; metal avg `-0.059` n `20`; unknown avg `1.2342` n `797`
- 1h: commodity avg `0.0564` n `12`; crypto_alt avg `0.1895` n `232`; crypto_major avg `0.0195` n `8`; equity avg `-0.3698` n `134`; fx avg `0.0111` n `6`; index avg `-0.0957` n `26`; metal avg `-0.1019` n `20`; unknown avg `0.1654` n `779`
- 4h: commodity avg `0.1699` n `12`; crypto_alt avg `-0.5157` n `232`; crypto_major avg `-0.6315` n `8`; equity avg `-0.1847` n `134`; fx avg `0.0453` n `6`; index avg `-0.0467` n `26`; metal avg `-0.1004` n `20`; unknown avg `0.1673` n `767`
- 24h: commodity avg `0.1506` n `12`; crypto_alt avg `0.4005` n `232`; crypto_major avg `-1.2566` n `8`; equity avg `0.2564` n `134`; fx avg `-0.2337` n `6`; index avg `0.0777` n `26`; metal avg `0.2382` n `20`; unknown avg `7464.4925` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
