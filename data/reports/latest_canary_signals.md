# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T23:56:12.956588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.129` n `13`; crypto_alt avg `-0.4629` n `235`; crypto_major avg `-0.3299` n `8`; equity avg `-0.0923` n `150`; fx avg `0.0155` n `6`; index avg `-0.0129` n `26`; metal avg `0.0159` n `20`; unknown avg `1.4141` n `1077`
- 1h: commodity avg `0.1435` n `13`; crypto_alt avg `-0.349` n `235`; crypto_major avg `-0.2621` n `8`; equity avg `-0.239` n `150`; fx avg `0.0312` n `6`; index avg `-0.0334` n `26`; metal avg `0.0648` n `20`; unknown avg `1.209` n `1075`
- 4h: commodity avg `0.0671` n `13`; crypto_alt avg `0.2884` n `235`; crypto_major avg `0.181` n `8`; equity avg `0.1866` n `150`; fx avg `0.0307` n `6`; index avg `0.0364` n `26`; metal avg `0.1185` n `20`; unknown avg `-0.1103` n `1007`
- 24h: commodity avg `0.6478` n `13`; crypto_alt avg `-3.4961` n `235`; crypto_major avg `-3.7389` n `8`; equity avg `-2.9909` n `150`; fx avg `0.0809` n `6`; index avg `-0.4041` n `26`; metal avg `0.0926` n `20`; unknown avg `6.6362` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
