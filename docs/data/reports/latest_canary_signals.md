# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T03:38:07.629974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.1928` n `233`; crypto_major avg `0.1368` n `8`; equity avg `0.0183` n `136`; fx avg `0.0038` n `6`; index avg `-0.0064` n `26`; metal avg `0.0269` n `20`; unknown avg `0.5226` n `794`
- 1h: commodity avg `0.0626` n `12`; crypto_alt avg `0.0903` n `233`; crypto_major avg `0.0013` n `8`; equity avg `-0.1738` n `136`; fx avg `-0.0264` n `6`; index avg `-0.0151` n `26`; metal avg `0.014` n `20`; unknown avg `0.2128` n `792`
- 4h: commodity avg `-0.1802` n `12`; crypto_alt avg `0.2015` n `233`; crypto_major avg `0.0661` n `8`; equity avg `-0.2351` n `136`; fx avg `-0.0704` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0414` n `20`; unknown avg `0.504` n `778`
- 24h: commodity avg `1.1884` n `12`; crypto_alt avg `-2.1859` n `233`; crypto_major avg `-2.4589` n `8`; equity avg `-2.0961` n `136`; fx avg `0.0803` n `6`; index avg `-0.3621` n `26`; metal avg `-1.3285` n `20`; unknown avg `-0.9357` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
