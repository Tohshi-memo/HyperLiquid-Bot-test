# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T00:22:19.032258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.77` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.2834` n `228`; crypto_major avg `-0.0747` n `8`; equity avg `-0.3428` n `69`; fx avg `-0.0184` n `6`; index avg `-0.1499` n `23`; metal avg `0.1773` n `18`; unknown avg `0.5491` n `422`
- 1h: commodity avg `-0.2133` n `12`; crypto_alt avg `-0.387` n `228`; crypto_major avg `-0.4203` n `8`; equity avg `-0.6961` n `69`; fx avg `0.0243` n `6`; index avg `-0.2711` n `23`; metal avg `0.0435` n `18`; unknown avg `0.6028` n `422`
- 4h: commodity avg `-0.2361` n `12`; crypto_alt avg `-0.6028` n `228`; crypto_major avg `-0.2752` n `8`; equity avg `-0.7698` n `69`; fx avg `0.0066` n `6`; index avg `-0.3766` n `23`; metal avg `0.1511` n `18`; unknown avg `1.2668` n `422`
- 24h: commodity avg `-0.2216` n `12`; crypto_alt avg `-0.6443` n `228`; crypto_major avg `-1.1252` n `8`; equity avg `-0.8395` n `69`; fx avg `0.0466` n `6`; index avg `-0.0979` n `23`; metal avg `-0.2851` n `18`; unknown avg `2.9016` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
