# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T10:37:34.150571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `0.0125` n `228`; crypto_major avg `-0.044` n `8`; equity avg `-0.0749` n `79`; fx avg `-0.0018` n `6`; index avg `-0.0072` n `23`; metal avg `-0.0116` n `18`; unknown avg `0.0094` n `701`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `0.1449` n `228`; crypto_major avg `0.0764` n `8`; equity avg `0.0412` n `79`; fx avg `0.0089` n `6`; index avg `0.0336` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.0153` n `701`
- 4h: commodity avg `0.1241` n `12`; crypto_alt avg `0.2139` n `228`; crypto_major avg `0.4422` n `8`; equity avg `0.2558` n `79`; fx avg `0.0167` n `6`; index avg `0.072` n `23`; metal avg `0.003` n `18`; unknown avg `-0.0948` n `693`
- 24h: commodity avg `-0.1508` n `12`; crypto_alt avg `-0.4108` n `228`; crypto_major avg `-0.2621` n `8`; equity avg `-0.127` n `79`; fx avg `0.0519` n `6`; index avg `0.064` n `23`; metal avg `0.4958` n `18`; unknown avg `0.1175` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
