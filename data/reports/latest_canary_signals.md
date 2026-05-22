# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T12:07:24.707202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1313` n `12`; crypto_alt avg `0.0987` n `228`; crypto_major avg `0.1656` n `8`; equity avg `-0.0567` n `67`; fx avg `0.0003` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0779` n `18`; unknown avg `0.112` n `386`
- 1h: commodity avg `-0.4103` n `12`; crypto_alt avg `0.4199` n `228`; crypto_major avg `0.5009` n `8`; equity avg `0.0843` n `67`; fx avg `0.001` n `6`; index avg `0.0427` n `23`; metal avg `-0.0014` n `18`; unknown avg `0.1045` n `386`
- 4h: commodity avg `-0.4633` n `12`; crypto_alt avg `0.399` n `228`; crypto_major avg `0.7648` n `8`; equity avg `-0.4594` n `67`; fx avg `-0.0136` n `6`; index avg `-0.1692` n `23`; metal avg `0.0704` n `18`; unknown avg `-0.2289` n `386`
- 24h: commodity avg `-1.2758` n `12`; crypto_alt avg `3.088` n `228`; crypto_major avg `1.5657` n `8`; equity avg `1.2322` n `67`; fx avg `0.0925` n `6`; index avg `0.8082` n `23`; metal avg `0.8277` n `18`; unknown avg `1.1881` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.04`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0391`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0366`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0339`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0301`, n `668`, weak_sample_signal
