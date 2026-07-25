# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T16:15:15.244661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.0229` n `230`; crypto_major avg `0.0949` n `8`; equity avg `0.0174` n `100`; fx avg `-0.0016` n `6`; index avg `-0.0056` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0081` n `774`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `0.1445` n `230`; crypto_major avg `0.1764` n `8`; equity avg `0.0007` n `100`; fx avg `-0.0031` n `6`; index avg `0.0066` n `25`; metal avg `-0.0172` n `20`; unknown avg `0.0131` n `774`
- 4h: commodity avg `-0.3429` n `12`; crypto_alt avg `0.6653` n `230`; crypto_major avg `0.8184` n `8`; equity avg `0.0059` n `100`; fx avg `-0.0032` n `6`; index avg `0.0111` n `25`; metal avg `0.013` n `20`; unknown avg `0.0195` n `774`
- 24h: commodity avg `-0.2988` n `12`; crypto_alt avg `0.1374` n `230`; crypto_major avg `0.5454` n `8`; equity avg `-1.5231` n `100`; fx avg `-0.0401` n `6`; index avg `-0.2175` n `25`; metal avg `-0.2388` n `20`; unknown avg `-0.3084` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1256`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1096`, n `666`, weak_sample_signal
