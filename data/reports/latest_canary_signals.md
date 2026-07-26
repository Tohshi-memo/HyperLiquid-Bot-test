# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T18:52:26.331247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `12`; crypto_alt avg `0.0602` n `230`; crypto_major avg `0.0914` n `8`; equity avg `0.0319` n `100`; fx avg `0.0071` n `6`; index avg `0.0023` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.1272` n `775`
- 1h: commodity avg `0.0848` n `12`; crypto_alt avg `-0.0673` n `230`; crypto_major avg `0.0304` n `8`; equity avg `0.059` n `100`; fx avg `0.0186` n `6`; index avg `-0.0193` n `25`; metal avg `0.03` n `20`; unknown avg `-0.1887` n `775`
- 4h: commodity avg `0.161` n `12`; crypto_alt avg `0.2107` n `230`; crypto_major avg `0.3355` n `8`; equity avg `0.1223` n `100`; fx avg `0.0007` n `6`; index avg `0.0079` n `25`; metal avg `0.0301` n `20`; unknown avg `-0.2184` n `775`
- 24h: commodity avg `-0.3651` n `12`; crypto_alt avg `0.7927` n `230`; crypto_major avg `0.682` n `8`; equity avg `0.7427` n `100`; fx avg `0.0509` n `6`; index avg `0.1366` n `25`; metal avg `0.1987` n `20`; unknown avg `-0.0659` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1926`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
