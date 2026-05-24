# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T21:22:16.817502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0589` n `12`; crypto_alt avg `-0.0457` n `228`; crypto_major avg `-0.0381` n `8`; equity avg `0.0056` n `67`; fx avg `0.0039` n `6`; index avg `0.0031` n `23`; metal avg `-0.0653` n `18`; unknown avg `-0.1354` n `396`
- 1h: commodity avg `0.0609` n `12`; crypto_alt avg `-0.1183` n `228`; crypto_major avg `-0.1562` n `8`; equity avg `0.0338` n `67`; fx avg `0.0122` n `6`; index avg `-0.0927` n `23`; metal avg `-0.1833` n `18`; unknown avg `-0.3086` n `396`
- 4h: commodity avg `0.1043` n `12`; crypto_alt avg `-0.4908` n `228`; crypto_major avg `-0.3633` n `8`; equity avg `0.1458` n `67`; fx avg `0.0523` n `6`; index avg `-0.0313` n `23`; metal avg `-0.2575` n `18`; unknown avg `-0.5226` n `396`
- 24h: commodity avg `1.6807` n `12`; crypto_alt avg `-2.5081` n `228`; crypto_major avg `-0.425` n `8`; equity avg `0.4199` n `67`; fx avg `0.1058` n `6`; index avg `-0.2544` n `23`; metal avg `-0.381` n `18`; unknown avg `0.0893` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
