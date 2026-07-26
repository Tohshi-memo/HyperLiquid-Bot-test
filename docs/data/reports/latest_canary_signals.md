# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T11:52:28.584358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0268` n `12`; crypto_alt avg `-0.0534` n `230`; crypto_major avg `-0.0974` n `8`; equity avg `0.0175` n `100`; fx avg `0.0015` n `6`; index avg `0.0051` n `25`; metal avg `0.0014` n `20`; unknown avg `0.0091` n `775`
- 1h: commodity avg `-0.026` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `-0.066` n `8`; equity avg `0.0624` n `100`; fx avg `-0.0035` n `6`; index avg `-0.0039` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.0047` n `775`
- 4h: commodity avg `-0.3356` n `12`; crypto_alt avg `0.0199` n `230`; crypto_major avg `0.0816` n `8`; equity avg `0.2598` n `100`; fx avg `-0.0388` n `6`; index avg `0.051` n `25`; metal avg `0.1183` n `20`; unknown avg `0.013` n `775`
- 24h: commodity avg `-0.8377` n `12`; crypto_alt avg `1.6752` n `230`; crypto_major avg `1.5839` n `8`; equity avg `0.8199` n `100`; fx avg `0.0181` n `6`; index avg `0.1812` n `25`; metal avg `0.1853` n `20`; unknown avg `0.1498` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.126`, n `667`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `667`, weak_sample_signal
