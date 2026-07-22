# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T12:22:24.759180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.0363` n `230`; crypto_major avg `-0.0155` n `8`; equity avg `-0.1394` n `98`; fx avg `0.0002` n `6`; index avg `-0.0239` n `25`; metal avg `0.0317` n `20`; unknown avg `-0.0876` n `773`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.2562` n `230`; crypto_major avg `-0.3988` n `8`; equity avg `-0.616` n `98`; fx avg `0.0029` n `6`; index avg `-0.1048` n `25`; metal avg `0.0566` n `20`; unknown avg `-0.0538` n `773`
- 4h: commodity avg `0.0792` n `12`; crypto_alt avg `0.0428` n `230`; crypto_major avg `-0.1585` n `8`; equity avg `-0.4873` n `98`; fx avg `-0.0217` n `6`; index avg `-0.0987` n `25`; metal avg `0.1021` n `20`; unknown avg `0.4529` n `773`
- 24h: commodity avg `0.5661` n `12`; crypto_alt avg `-0.8433` n `230`; crypto_major avg `-1.6561` n `8`; equity avg `-0.0366` n `98`; fx avg `-0.0157` n `6`; index avg `-0.1265` n `25`; metal avg `0.4295` n `20`; unknown avg `0.5339` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1043`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
