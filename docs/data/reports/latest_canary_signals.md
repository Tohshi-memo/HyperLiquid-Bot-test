# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T12:52:29.105047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0326` n `12`; crypto_alt avg `0.1269` n `230`; crypto_major avg `0.1752` n `8`; equity avg `0.096` n `102`; fx avg `-0.007` n `6`; index avg `0.0103` n `25`; metal avg `0.0622` n `20`; unknown avg `0.2019` n `774`
- 1h: commodity avg `-0.112` n `12`; crypto_alt avg `0.2201` n `230`; crypto_major avg `0.2067` n `8`; equity avg `0.2382` n `102`; fx avg `0.0103` n `6`; index avg `0.0854` n `25`; metal avg `0.1828` n `20`; unknown avg `0.2633` n `774`
- 4h: commodity avg `0.1817` n `12`; crypto_alt avg `0.0472` n `230`; crypto_major avg `-0.1104` n `8`; equity avg `-0.6979` n `102`; fx avg `-0.0438` n `6`; index avg `-0.0429` n `25`; metal avg `-0.071` n `20`; unknown avg `0.0391` n `774`
- 24h: commodity avg `-0.7516` n `12`; crypto_alt avg `-3.3521` n `230`; crypto_major avg `-3.5678` n `8`; equity avg `-4.2836` n `102`; fx avg `-0.1666` n `6`; index avg `-0.813` n `25`; metal avg `-0.436` n `20`; unknown avg `1225.3459` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
