# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T16:52:34.170943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.0552` n `230`; crypto_major avg `0.0823` n `8`; equity avg `-0.0004` n `100`; fx avg `0.0129` n `6`; index avg `0.0027` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0576` n `774`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `0.0972` n `230`; crypto_major avg `0.2321` n `8`; equity avg `-0.0018` n `100`; fx avg `-0.0076` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0166` n `20`; unknown avg `-0.0366` n `774`
- 4h: commodity avg `-0.3605` n `12`; crypto_alt avg `0.5362` n `230`; crypto_major avg `0.8225` n `8`; equity avg `0.0094` n `100`; fx avg `-0.0062` n `6`; index avg `-0.0017` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.0115` n `774`
- 24h: commodity avg `-0.2207` n `12`; crypto_alt avg `0.4468` n `230`; crypto_major avg `1.0484` n `8`; equity avg `-0.797` n `100`; fx avg `-0.022` n `6`; index avg `-0.0903` n `25`; metal avg `-0.1181` n `20`; unknown avg `-0.3645` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1274`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1114`, n `666`, weak_sample_signal
