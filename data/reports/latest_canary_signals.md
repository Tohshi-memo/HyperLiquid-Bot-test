# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T00:52:19.212660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1164` n `12`; crypto_alt avg `-0.1996` n `228`; crypto_major avg `-0.2018` n `8`; equity avg `-0.2663` n `69`; fx avg `0.0123` n `6`; index avg `-0.1781` n `23`; metal avg `-0.1624` n `18`; unknown avg `-0.1467` n `422`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `-0.3048` n `228`; crypto_major avg `-0.1606` n `8`; equity avg `-0.6519` n `69`; fx avg `0.0327` n `6`; index avg `-0.3495` n `23`; metal avg `-0.0789` n `18`; unknown avg `-0.2173` n `422`
- 4h: commodity avg `-0.2322` n `12`; crypto_alt avg `-0.46` n `228`; crypto_major avg `0.0491` n `8`; equity avg `-0.7854` n `69`; fx avg `0.0099` n `6`; index avg `-0.4697` n `23`; metal avg `0.0351` n `18`; unknown avg `-0.0286` n `422`
- 24h: commodity avg `-0.0608` n `12`; crypto_alt avg `-1.0639` n `228`; crypto_major avg `-1.6578` n `8`; equity avg `-0.9964` n `69`; fx avg `0.0247` n `6`; index avg `-0.5498` n `23`; metal avg `-0.4587` n `18`; unknown avg `1.3903` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
