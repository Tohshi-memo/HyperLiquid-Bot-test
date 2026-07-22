# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T23:48:24.606013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.079` n `230`; crypto_major avg `0.1004` n `8`; equity avg `0.1265` n `98`; fx avg `-0.0024` n `6`; index avg `0.0232` n `25`; metal avg `0.04` n `20`; unknown avg `-0.0241` n `773`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1558` n `230`; crypto_major avg `-0.0116` n `8`; equity avg `0.1459` n `98`; fx avg `0.0139` n `6`; index avg `0.0485` n `25`; metal avg `0.0738` n `20`; unknown avg `0.0626` n `773`
- 4h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.0121` n `230`; crypto_major avg `0.2034` n `8`; equity avg `0.1949` n `98`; fx avg `-0.0054` n `6`; index avg `0.0015` n `25`; metal avg `-0.0473` n `20`; unknown avg `0.1377` n `773`
- 24h: commodity avg `0.6648` n `12`; crypto_alt avg `-0.5534` n `230`; crypto_major avg `-0.5592` n `8`; equity avg `-1.1369` n `98`; fx avg `-0.057` n `6`; index avg `-0.1625` n `25`; metal avg `0.1946` n `20`; unknown avg `1.656` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0933`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
