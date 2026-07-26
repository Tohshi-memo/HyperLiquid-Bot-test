# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T10:52:30.800239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `-0.064` n `230`; crypto_major avg `-0.0719` n `8`; equity avg `0.0214` n `100`; fx avg `0.001` n `6`; index avg `-0.004` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0228` n `775`
- 1h: commodity avg `-0.1696` n `12`; crypto_alt avg `0.0711` n `230`; crypto_major avg `0.0155` n `8`; equity avg `0.1686` n `100`; fx avg `0.0056` n `6`; index avg `0.0436` n `25`; metal avg `0.0542` n `20`; unknown avg `0.0826` n `775`
- 4h: commodity avg `-0.4367` n `12`; crypto_alt avg `0.0989` n `230`; crypto_major avg `0.0444` n `8`; equity avg `0.1559` n `100`; fx avg `-0.0384` n `6`; index avg `0.0594` n `25`; metal avg `0.1282` n `20`; unknown avg `-0.0511` n `775`
- 24h: commodity avg `-0.8671` n `12`; crypto_alt avg `1.577` n `230`; crypto_major avg `1.6604` n `8`; equity avg `0.7368` n `100`; fx avg `0.012` n `6`; index avg `0.1744` n `25`; metal avg `0.1746` n `20`; unknown avg `0.1111` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1461`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1354`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1308`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.125`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1245`, n `666`, weak_sample_signal
