# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T19:22:23.393704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0814` n `230`; crypto_major avg `-0.0684` n `8`; equity avg `0.0215` n `100`; fx avg `0.005` n `6`; index avg `0.0061` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.043` n `774`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.1164` n `230`; crypto_major avg `-0.0225` n `8`; equity avg `0.0377` n `100`; fx avg `0.016` n `6`; index avg `-0.0022` n `25`; metal avg `0.0079` n `20`; unknown avg `-0.0914` n `774`
- 4h: commodity avg `-0.0553` n `12`; crypto_alt avg `0.3466` n `230`; crypto_major avg `0.6565` n `8`; equity avg `0.2068` n `100`; fx avg `-0.0061` n `6`; index avg `0.0502` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.1245` n `774`
- 24h: commodity avg `-0.4482` n `12`; crypto_alt avg `0.4277` n `230`; crypto_major avg `1.0856` n `8`; equity avg `0.4281` n `100`; fx avg `-0.0139` n `6`; index avg `0.1371` n `25`; metal avg `0.048` n `20`; unknown avg `-0.2919` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1718`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1314`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1162`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1137`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
