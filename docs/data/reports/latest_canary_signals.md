# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T13:52:21.812354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `12`; crypto_alt avg `0.2444` n `228`; crypto_major avg `0.0097` n `8`; equity avg `0.0336` n `67`; fx avg `-0.0075` n `6`; index avg `-0.1225` n `23`; metal avg `0.2518` n `18`; unknown avg `-0.3254` n `418`
- 1h: commodity avg `0.4785` n `12`; crypto_alt avg `-0.6805` n `228`; crypto_major avg `-0.804` n `8`; equity avg `-0.6884` n `67`; fx avg `-0.0346` n `6`; index avg `-0.618` n `23`; metal avg `-0.0988` n `18`; unknown avg `0.2084` n `418`
- 4h: commodity avg `0.2937` n `12`; crypto_alt avg `0.0022` n `228`; crypto_major avg `-0.9003` n `8`; equity avg `-0.8063` n `67`; fx avg `-0.0252` n `6`; index avg `-0.575` n `23`; metal avg `-0.7285` n `18`; unknown avg `0.371` n `418`
- 24h: commodity avg `-1.8008` n `12`; crypto_alt avg `-2.6284` n `228`; crypto_major avg `-2.219` n `8`; equity avg `-0.142` n `67`; fx avg `-0.0438` n `6`; index avg `-0.2793` n `23`; metal avg `-1.1705` n `18`; unknown avg `0.3018` n `398`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
