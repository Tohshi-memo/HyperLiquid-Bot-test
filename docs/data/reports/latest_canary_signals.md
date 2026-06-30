# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T01:34:24.039435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.2113` n `228`; crypto_major avg `0.2363` n `8`; equity avg `0.1635` n `88`; fx avg `0.0053` n `6`; index avg `0.0533` n `23`; metal avg `0.1182` n `20`; unknown avg `0.0369` n `765`
- 1h: commodity avg `0.0236` n `12`; crypto_alt avg `0.1705` n `228`; crypto_major avg `0.2711` n `8`; equity avg `0.3175` n `88`; fx avg `0.0037` n `6`; index avg `0.0983` n `23`; metal avg `-0.1714` n `20`; unknown avg `1.4484` n `765`
- 4h: commodity avg `-0.0339` n `12`; crypto_alt avg `-0.8934` n `228`; crypto_major avg `-1.0023` n `8`; equity avg `-0.1715` n `88`; fx avg `0.0594` n `6`; index avg `-0.0763` n `23`; metal avg `-0.366` n `20`; unknown avg `0.1653` n `763`
- 24h: commodity avg `-0.2894` n `12`; crypto_alt avg `0.8106` n `228`; crypto_major avg `2.1358` n `8`; equity avg `1.9736` n `88`; fx avg `0.2121` n `6`; index avg `0.2384` n `23`; metal avg `-0.5855` n `20`; unknown avg `2.2894` n `730`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
