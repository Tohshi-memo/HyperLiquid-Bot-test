# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T06:37:26.785838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0868` n `12`; crypto_alt avg `0.1362` n `230`; crypto_major avg `0.1443` n `8`; equity avg `0.0161` n `100`; fx avg `0.0005` n `6`; index avg `0.0021` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.0288` n `775`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `-0.1764` n `8`; equity avg `0.0013` n `100`; fx avg `0.0051` n `6`; index avg `0.0051` n `25`; metal avg `0.0046` n `20`; unknown avg `-0.0047` n `759`
- 4h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.4208` n `230`; crypto_major avg `0.1553` n `8`; equity avg `0.045` n `100`; fx avg `0.0681` n `6`; index avg `0.0006` n `25`; metal avg `0.0056` n `20`; unknown avg `0.0162` n `758`
- 24h: commodity avg `-0.5161` n `12`; crypto_alt avg `1.4625` n `230`; crypto_major avg `1.6645` n `8`; equity avg `0.4209` n `100`; fx avg `0.0583` n `6`; index avg `0.1142` n `25`; metal avg `0.045` n `20`; unknown avg `-0.0974` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.138`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1203`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
