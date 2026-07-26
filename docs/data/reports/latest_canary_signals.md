# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T07:27:47.481985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `-0.064` n `230`; crypto_major avg `-0.0824` n `8`; equity avg `-0.0441` n `100`; fx avg `-0.0063` n `6`; index avg `-0.0015` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0334` n `775`
- 1h: commodity avg `-0.1574` n `12`; crypto_alt avg `0.4018` n `230`; crypto_major avg `0.3089` n `8`; equity avg `0.0547` n `100`; fx avg `-0.0038` n `6`; index avg `0.0071` n `25`; metal avg `0.0111` n `20`; unknown avg `0.0244` n `775`
- 4h: commodity avg `-0.0899` n `12`; crypto_alt avg `0.4463` n `230`; crypto_major avg `0.2198` n `8`; equity avg `0.0261` n `100`; fx avg `0.0533` n `6`; index avg `0.0048` n `25`; metal avg `0.0203` n `20`; unknown avg `-0.0075` n `759`
- 24h: commodity avg `-0.6153` n `12`; crypto_alt avg `1.6174` n `230`; crypto_major avg `1.7657` n `8`; equity avg `0.5178` n `100`; fx avg `0.0175` n `6`; index avg `0.1355` n `25`; metal avg `0.0519` n `20`; unknown avg `-0.1211` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1839`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1398`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1247`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1221`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.118`, n `666`, weak_sample_signal
