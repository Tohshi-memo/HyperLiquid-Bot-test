# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T21:07:27.425610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `0.0405` n `230`; crypto_major avg `0.0182` n `8`; equity avg `0.0288` n `100`; fx avg `-0.0126` n `6`; index avg `-0.0` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0068` n `775`
- 1h: commodity avg `0.0691` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.0535` n `8`; equity avg `0.0709` n `100`; fx avg `-0.0018` n `6`; index avg `-0.0012` n `25`; metal avg `0.0119` n `20`; unknown avg `0.0783` n `775`
- 4h: commodity avg `0.3047` n `12`; crypto_alt avg `-0.2382` n `230`; crypto_major avg `-0.2188` n `8`; equity avg `-0.0321` n `100`; fx avg `0.0285` n `6`; index avg `-0.0405` n `25`; metal avg `0.0186` n `20`; unknown avg `-0.0883` n `775`
- 24h: commodity avg `-0.1192` n `12`; crypto_alt avg `0.8285` n `230`; crypto_major avg `0.8778` n `8`; equity avg `0.639` n `100`; fx avg `0.0389` n `6`; index avg `0.0981` n `25`; metal avg `0.202` n `20`; unknown avg `-0.0779` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
