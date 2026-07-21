# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T03:22:24.283195+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.0087` n `230`; crypto_major avg `-0.1644` n `8`; equity avg `0.2034` n `98`; fx avg `0.0063` n `6`; index avg `0.0274` n `25`; metal avg `-0.0083` n `20`; unknown avg `0.0046` n `771`
- 1h: commodity avg `0.0108` n `12`; crypto_alt avg `0.5678` n `230`; crypto_major avg `0.5389` n `8`; equity avg `0.9261` n `98`; fx avg `-0.0297` n `6`; index avg `0.1403` n `25`; metal avg `0.1854` n `20`; unknown avg `1.7618` n `771`
- 4h: commodity avg `-0.0284` n `12`; crypto_alt avg `0.5302` n `230`; crypto_major avg `0.5556` n `8`; equity avg `0.8453` n `98`; fx avg `0.0255` n `6`; index avg `0.2047` n `25`; metal avg `0.3167` n `20`; unknown avg `0.7091` n `770`
- 24h: commodity avg `-0.3106` n `12`; crypto_alt avg `1.8099` n `230`; crypto_major avg `1.5272` n `8`; equity avg `0.702` n `98`; fx avg `-0.1215` n `6`; index avg `0.2158` n `25`; metal avg `0.1782` n `20`; unknown avg `0.0384` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0812`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
