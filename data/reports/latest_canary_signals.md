# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T10:37:19.926037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1923` n `12`; crypto_alt avg `-0.0217` n `228`; crypto_major avg `0.0314` n `8`; equity avg `-0.0448` n `67`; fx avg `-0.0059` n `6`; index avg `0.0132` n `23`; metal avg `-0.0786` n `18`; unknown avg `0.0231` n `418`
- 1h: commodity avg `0.2129` n `12`; crypto_alt avg `0.0432` n `228`; crypto_major avg `0.0635` n `8`; equity avg `0.056` n `67`; fx avg `-0.0256` n `6`; index avg `0.068` n `23`; metal avg `-0.1148` n `18`; unknown avg `0.0805` n `418`
- 4h: commodity avg `-0.5332` n `12`; crypto_alt avg `-0.232` n `228`; crypto_major avg `0.2884` n `8`; equity avg `0.7297` n `67`; fx avg `-0.0529` n `6`; index avg `0.2603` n `23`; metal avg `0.1722` n `18`; unknown avg `-0.0223` n `418`
- 24h: commodity avg `-0.9025` n `12`; crypto_alt avg `-2.2398` n `228`; crypto_major avg `-0.8716` n `8`; equity avg `0.6218` n `67`; fx avg `-0.0558` n `6`; index avg `0.6807` n `23`; metal avg `-0.6857` n `18`; unknown avg `0.2539` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1939`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
