# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T15:22:25.584748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.1497` n `230`; crypto_major avg `0.1586` n `8`; equity avg `0.0526` n `100`; fx avg `0.0006` n `6`; index avg `0.0071` n `25`; metal avg `0.004` n `20`; unknown avg `-0.0081` n `775`
- 1h: commodity avg `-0.0603` n `12`; crypto_alt avg `0.1835` n `230`; crypto_major avg `0.2933` n `8`; equity avg `0.0826` n `100`; fx avg `-0.0039` n `6`; index avg `0.0071` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0104` n `775`
- 4h: commodity avg `-0.0034` n `12`; crypto_alt avg `0.0306` n `230`; crypto_major avg `0.3077` n `8`; equity avg `0.1457` n `100`; fx avg `0.0021` n `6`; index avg `0.0285` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0746` n `775`
- 24h: commodity avg `-0.4632` n `12`; crypto_alt avg `1.1257` n `230`; crypto_major avg `1.3941` n `8`; equity avg `0.8928` n `100`; fx avg `0.0199` n `6`; index avg `0.1939` n `25`; metal avg `0.1628` n `20`; unknown avg `0.1358` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1814`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
