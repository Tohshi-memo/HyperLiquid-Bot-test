# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T09:37:26.055643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.1218` n `230`; crypto_major avg `0.0738` n `8`; equity avg `-0.0355` n `100`; fx avg `-0.0117` n `6`; index avg `0.0042` n `25`; metal avg `0.0061` n `20`; unknown avg `0.003` n `774`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `0.068` n `230`; crypto_major avg `0.1046` n `8`; equity avg `-0.0498` n `100`; fx avg `0.0016` n `6`; index avg `0.0178` n `25`; metal avg `0.0047` n `20`; unknown avg `0.3577` n `774`
- 4h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.2441` n `230`; crypto_major avg `-0.0645` n `8`; equity avg `-0.1208` n `100`; fx avg `0.016` n `6`; index avg `0.007` n `25`; metal avg `0.0103` n `20`; unknown avg `-0.2311` n `758`
- 24h: commodity avg `0.1538` n `12`; crypto_alt avg `-1.6326` n `230`; crypto_major avg `-1.277` n `8`; equity avg `-2.9993` n `100`; fx avg `-0.022` n `6`; index avg `-0.262` n `25`; metal avg `-0.0889` n `20`; unknown avg `13.1527` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1165`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1007`, n `666`, weak_sample_signal
