# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T11:22:25.692410+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0421` n `12`; crypto_alt avg `0.0455` n `229`; crypto_major avg `-0.0571` n `8`; equity avg `-0.079` n `91`; fx avg `0.0097` n `6`; index avg `-0.0011` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0247` n `763`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `0.264` n `229`; crypto_major avg `0.1063` n `8`; equity avg `0.2109` n `91`; fx avg `0.0209` n `6`; index avg `0.0499` n `25`; metal avg `-0.1243` n `20`; unknown avg `-0.0117` n `763`
- 4h: commodity avg `0.5001` n `12`; crypto_alt avg `-0.9519` n `229`; crypto_major avg `-0.5882` n `8`; equity avg `-1.3533` n `91`; fx avg `0.0457` n `6`; index avg `-0.2871` n `25`; metal avg `-1.0155` n `20`; unknown avg `-0.1526` n `763`
- 24h: commodity avg `1.2234` n `12`; crypto_alt avg `-3.7952` n `229`; crypto_major avg `-2.9456` n `8`; equity avg `-2.8879` n `91`; fx avg `-0.0836` n `6`; index avg `-0.6041` n `25`; metal avg `-1.3659` n `20`; unknown avg `-0.8427` n `733`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
