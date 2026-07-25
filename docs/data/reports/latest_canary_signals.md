# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T22:52:31.664693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.0447` n `230`; crypto_major avg `0.0315` n `8`; equity avg `0.0046` n `100`; fx avg `-0.0032` n `6`; index avg `0.0027` n `25`; metal avg `-0.0018` n `20`; unknown avg `-0.0408` n `774`
- 1h: commodity avg `-0.0913` n `12`; crypto_alt avg `-0.0192` n `230`; crypto_major avg `0.0094` n `8`; equity avg `0.0578` n `100`; fx avg `-0.004` n `6`; index avg `0.0108` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.1174` n `774`
- 4h: commodity avg `-0.0947` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `-0.2443` n `8`; equity avg `0.0868` n `100`; fx avg `0.0184` n `6`; index avg `0.0236` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.0659` n `774`
- 24h: commodity avg `-0.6467` n `12`; crypto_alt avg `0.5981` n `230`; crypto_major avg `1.1548` n `8`; equity avg `0.3629` n `100`; fx avg `0.0022` n `6`; index avg `0.1497` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.2927` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1166`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1154`, n `666`, weak_sample_signal
