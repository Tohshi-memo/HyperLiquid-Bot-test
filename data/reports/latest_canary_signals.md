# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T13:52:26.837257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.002` n `12`; crypto_alt avg `-0.0007` n `230`; crypto_major avg `-0.0029` n `8`; equity avg `0.323` n `113`; fx avg `0.0046` n `6`; index avg `0.0447` n `25`; metal avg `0.0919` n `20`; unknown avg `0.0518` n `786`
- 1h: commodity avg `-0.1038` n `12`; crypto_alt avg `-0.1312` n `230`; crypto_major avg `-0.2497` n `8`; equity avg `0.1892` n `113`; fx avg `-0.022` n `6`; index avg `0.0403` n `25`; metal avg `-0.0367` n `20`; unknown avg `0.0626` n `786`
- 4h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.1113` n `230`; crypto_major avg `-0.2871` n `8`; equity avg `0.9874` n `113`; fx avg `0.0202` n `6`; index avg `0.1487` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.0804` n `786`
- 24h: commodity avg `0.2321` n `12`; crypto_alt avg `-0.7871` n `230`; crypto_major avg `0.5501` n `8`; equity avg `3.3838` n `113`; fx avg `0.069` n `6`; index avg `0.3858` n `25`; metal avg `0.3235` n `20`; unknown avg `-0.0683` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2092`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
