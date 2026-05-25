# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T21:37:20.483277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3935` n `12`; crypto_alt avg `0.1927` n `228`; crypto_major avg `-0.0694` n `8`; equity avg `0.0465` n `67`; fx avg `-0.0239` n `6`; index avg `0.0755` n `23`; metal avg `0.0005` n `18`; unknown avg `0.1871` n `405`
- 1h: commodity avg `0.4152` n `12`; crypto_alt avg `-0.0924` n `228`; crypto_major avg `-0.117` n `8`; equity avg `-0.0005` n `67`; fx avg `0.0343` n `6`; index avg `0.056` n `23`; metal avg `-0.0072` n `18`; unknown avg `-0.1115` n `405`
- 4h: commodity avg `0.631` n `12`; crypto_alt avg `-0.7013` n `228`; crypto_major avg `-0.5959` n `8`; equity avg `0.0435` n `67`; fx avg `0.0349` n `6`; index avg `0.1082` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.5406` n `405`
- 24h: commodity avg `-0.7695` n `12`; crypto_alt avg `3.2528` n `228`; crypto_major avg `1.06` n `8`; equity avg `1.0101` n `67`; fx avg `-0.0467` n `6`; index avg `0.7641` n `23`; metal avg `1.9999` n `18`; unknown avg `1.458` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
