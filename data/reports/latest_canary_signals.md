# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T02:22:31.210648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `-0.0904` n `230`; crypto_major avg `-0.1526` n `8`; equity avg `-0.3327` n `98`; fx avg `0.0018` n `6`; index avg `-0.074` n `25`; metal avg `-0.0214` n `20`; unknown avg `0.007` n `773`
- 1h: commodity avg `-0.0176` n `12`; crypto_alt avg `-0.2847` n `230`; crypto_major avg `-0.3646` n `8`; equity avg `-0.6688` n `98`; fx avg `-0.0258` n `6`; index avg `-0.1241` n `25`; metal avg `-0.1247` n `20`; unknown avg `0.1739` n `773`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `-0.4568` n `230`; crypto_major avg `-0.368` n `8`; equity avg `-0.1718` n `98`; fx avg `-0.0639` n `6`; index avg `0.015` n `25`; metal avg `0.0789` n `20`; unknown avg `-0.0224` n `773`
- 24h: commodity avg `0.6759` n `12`; crypto_alt avg `-0.9785` n `230`; crypto_major avg `-1.1401` n `8`; equity avg `-1.1737` n `98`; fx avg `-0.1407` n `6`; index avg `-0.1894` n `25`; metal avg `-0.175` n `20`; unknown avg `1.7257` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
