# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T15:37:45.992752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `0.0051` n `230`; crypto_major avg `0.0147` n `8`; equity avg `0.0089` n `100`; fx avg `0.0034` n `6`; index avg `0.0082` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0097` n `774`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.2527` n `230`; crypto_major avg `0.3763` n `8`; equity avg `0.0162` n `100`; fx avg `0.001` n `6`; index avg `-0.0036` n `25`; metal avg `0.0086` n `20`; unknown avg `0.2966` n `774`
- 4h: commodity avg `-0.4246` n `12`; crypto_alt avg `0.6111` n `230`; crypto_major avg `0.668` n `8`; equity avg `0.1048` n `100`; fx avg `-0.0009` n `6`; index avg `0.0112` n `25`; metal avg `0.018` n `20`; unknown avg `0.0289` n `774`
- 24h: commodity avg `-0.3322` n `12`; crypto_alt avg `-0.0616` n `230`; crypto_major avg `0.288` n `8`; equity avg `-1.0383` n `100`; fx avg `-0.045` n `6`; index avg `-0.1519` n `25`; metal avg `-0.1729` n `20`; unknown avg `-0.3266` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1646`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1245`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1086`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
