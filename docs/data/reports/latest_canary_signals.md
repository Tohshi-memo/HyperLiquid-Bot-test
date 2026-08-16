# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T21:52:23.804455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.4002` n `230`; crypto_major avg `-0.2778` n `8`; equity avg `-0.0244` n `114`; fx avg `-0.0019` n `6`; index avg `0.0166` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0292` n `791`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.6293` n `230`; crypto_major avg `-0.3287` n `8`; equity avg `-0.0075` n `114`; fx avg `-0.0015` n `6`; index avg `0.0146` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.077` n `791`
- 4h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.9239` n `230`; crypto_major avg `-0.5528` n `8`; equity avg `0.0074` n `114`; fx avg `0.0021` n `6`; index avg `0.0254` n `25`; metal avg `-0.0477` n `20`; unknown avg `0.0256` n `791`
- 24h: commodity avg `0.0626` n `12`; crypto_alt avg `-1.1297` n `230`; crypto_major avg `-0.5623` n `8`; equity avg `0.254` n `114`; fx avg `-0.0083` n `6`; index avg `0.0525` n `25`; metal avg `0.0016` n `20`; unknown avg `0.0082` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
