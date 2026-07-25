# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T18:35:03.906982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1307` n `12`; crypto_alt avg `-0.0085` n `230`; crypto_major avg `0.0622` n `8`; equity avg `0.0457` n `100`; fx avg `-0.0051` n `6`; index avg `0.0033` n `25`; metal avg `0.003` n `20`; unknown avg `-0.0622` n `774`
- 1h: commodity avg `0.0766` n `12`; crypto_alt avg `0.0171` n `230`; crypto_major avg `0.1248` n `8`; equity avg `0.0726` n `100`; fx avg `-0.0206` n `6`; index avg `0.0092` n `25`; metal avg `0.0143` n `20`; unknown avg `-0.0191` n `774`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `0.7063` n `230`; crypto_major avg `1.1092` n `8`; equity avg `0.2227` n `100`; fx avg `-0.0295` n `6`; index avg `0.0439` n `25`; metal avg `0.0174` n `20`; unknown avg `0.2967` n `774`
- 24h: commodity avg `-0.2493` n `12`; crypto_alt avg `0.633` n `230`; crypto_major avg `1.3987` n `8`; equity avg `0.1808` n `100`; fx avg `-0.0278` n `6`; index avg `0.1006` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.2771` n `757`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1299`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1189`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1125`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1117`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
