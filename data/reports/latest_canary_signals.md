# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T14:37:22.914593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2749` n `12`; crypto_alt avg `0.188` n `228`; crypto_major avg `0.1252` n `8`; equity avg `-0.0571` n `67`; fx avg `-0.0035` n `6`; index avg `-0.2073` n `23`; metal avg `-0.1514` n `18`; unknown avg `0.7845` n `418`
- 1h: commodity avg `0.265` n `12`; crypto_alt avg `0.09` n `228`; crypto_major avg `-0.1692` n `8`; equity avg `-0.009` n `67`; fx avg `0.0192` n `6`; index avg `-0.5019` n `23`; metal avg `0.278` n `18`; unknown avg `-0.3811` n `418`
- 4h: commodity avg `0.2746` n `12`; crypto_alt avg `-0.3445` n `228`; crypto_major avg `-1.1625` n `8`; equity avg `-0.8482` n `67`; fx avg `0.0279` n `6`; index avg `-0.9848` n `23`; metal avg `-0.5257` n `18`; unknown avg `0.9786` n `418`
- 24h: commodity avg `-1.2025` n `12`; crypto_alt avg `-2.9573` n `228`; crypto_major avg `-2.5208` n `8`; equity avg `-0.4885` n `67`; fx avg `0.0006` n `6`; index avg `-0.752` n `23`; metal avg `-1.303` n `18`; unknown avg `0.7888` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
