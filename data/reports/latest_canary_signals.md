# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T14:12:43.092982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `0.127` n `230`; crypto_major avg `0.2487` n `8`; equity avg `0.0784` n `100`; fx avg `0.0006` n `6`; index avg `0.0185` n `25`; metal avg `0.018` n `20`; unknown avg `0.1608` n `775`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `0.0808` n `230`; crypto_major avg `0.3581` n `8`; equity avg `0.1509` n `100`; fx avg `-0.0029` n `6`; index avg `0.0236` n `25`; metal avg `0.0292` n `20`; unknown avg `0.1772` n `775`
- 4h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `0.1466` n `8`; equity avg `0.2526` n `100`; fx avg `0.0092` n `6`; index avg `0.0468` n `25`; metal avg `0.0897` n `20`; unknown avg `0.0063` n `775`
- 24h: commodity avg `-0.4043` n `12`; crypto_alt avg `1.296` n `230`; crypto_major avg `1.6748` n `8`; equity avg `0.8937` n `100`; fx avg `0.0202` n `6`; index avg `0.1893` n `25`; metal avg `0.2036` n `20`; unknown avg `0.1596` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
