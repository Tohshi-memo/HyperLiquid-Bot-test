# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T06:22:17.357140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `-0.2357` n `228`; crypto_major avg `-0.1493` n `8`; equity avg `-0.0233` n `67`; fx avg `-0.0006` n `6`; index avg `-0.0444` n `23`; metal avg `-0.2636` n `18`; unknown avg `0.8906` n `418`
- 1h: commodity avg `-0.0905` n `12`; crypto_alt avg `0.1628` n `228`; crypto_major avg `0.1384` n `8`; equity avg `-0.0885` n `67`; fx avg `0.017` n `6`; index avg `-0.0892` n `23`; metal avg `-0.8019` n `18`; unknown avg `0.2432` n `400`
- 4h: commodity avg `-0.2717` n `12`; crypto_alt avg `0.1295` n `228`; crypto_major avg `0.4107` n `8`; equity avg `-0.4071` n `67`; fx avg `-0.0078` n `6`; index avg `-0.2673` n `23`; metal avg `-0.7852` n `18`; unknown avg `0.287` n `400`
- 24h: commodity avg `-0.3239` n `12`; crypto_alt avg `-1.0834` n `228`; crypto_major avg `-0.4592` n `8`; equity avg `0.2581` n `67`; fx avg `-0.0126` n `6`; index avg `0.7056` n `23`; metal avg `-0.8893` n `18`; unknown avg `1.5833` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1841`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1577`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
