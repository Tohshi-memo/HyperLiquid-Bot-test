# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T05:07:13.802037+00:00`
- Correlation status: `ready`
- Asset price records: `616`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0619` n `12`; crypto_alt avg `0.0742` n `228`; crypto_major avg `-0.0105` n `8`; equity avg `-0.0278` n `65`; fx avg `-0.0127` n `5`; index avg `0.0185` n `23`; metal avg `0.0311` n `18`; unknown avg `-0.2668` n `365`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.0266` n `228`; crypto_major avg `-0.1026` n `8`; equity avg `0.1075` n `65`; fx avg `0.0279` n `5`; index avg `0.0329` n `23`; metal avg `-0.0785` n `18`; unknown avg `-0.4951` n `365`
- 4h: commodity avg `-0.2704` n `12`; crypto_alt avg `0.2691` n `228`; crypto_major avg `-0.2284` n `8`; equity avg `0.161` n `65`; fx avg `0.0576` n `5`; index avg `0.0779` n `23`; metal avg `0.0646` n `18`; unknown avg `-0.7059` n `365`
- 24h: commodity avg `0.3566` n `12`; crypto_alt avg `1.5704` n `228`; crypto_major avg `-1.4855` n `8`; equity avg `-0.9619` n `65`; fx avg `0.2212` n `5`; index avg `-0.5929` n `23`; metal avg `0.3596` n `18`; unknown avg `-0.457` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1323`, n `612`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1213`, n `608`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.121`, n `608`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `612`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `612`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `612`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `608`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `608`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0789`, n `608`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0758`, n `612`, weak_sample_signal
