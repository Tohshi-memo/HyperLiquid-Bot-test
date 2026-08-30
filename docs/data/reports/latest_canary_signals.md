# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T02:37:29.891526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.0299` n `231`; crypto_major avg `-0.0227` n `8`; equity avg `-0.011` n `128`; fx avg `0.0027` n `6`; index avg `0.0029` n `26`; metal avg `0.0012` n `20`; unknown avg `0.0986` n `793`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.1043` n `231`; crypto_major avg `0.0816` n `8`; equity avg `0.014` n `128`; fx avg `0.002` n `6`; index avg `-0.0189` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.1092` n `793`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0948` n `231`; crypto_major avg `-0.0217` n `8`; equity avg `0.0205` n `128`; fx avg `0.0238` n `6`; index avg `0.0157` n `26`; metal avg `0.0047` n `20`; unknown avg `3.4574` n `793`
- 24h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.3845` n `231`; crypto_major avg `0.9577` n `8`; equity avg `0.371` n `128`; fx avg `-0.0075` n `6`; index avg `0.0778` n `26`; metal avg `0.0994` n `20`; unknown avg `0.0678` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
