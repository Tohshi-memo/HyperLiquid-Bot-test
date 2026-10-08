# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T20:52:24.136148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0745` n `13`; crypto_alt avg `0.144` n `235`; crypto_major avg `0.1126` n `8`; equity avg `-0.0122` n `150`; fx avg `-0.0127` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.1478` n `1077`
- 1h: commodity avg `0.0072` n `13`; crypto_alt avg `0.6378` n `235`; crypto_major avg `0.3217` n `8`; equity avg `0.2853` n `150`; fx avg `-0.0112` n `6`; index avg `0.0395` n `26`; metal avg `0.0` n `20`; unknown avg `0.4413` n `1013`
- 4h: commodity avg `0.0875` n `13`; crypto_alt avg `1.8743` n `235`; crypto_major avg `1.343` n `8`; equity avg `0.2893` n `150`; fx avg `0.0223` n `6`; index avg `0.031` n `26`; metal avg `0.0951` n `20`; unknown avg `0.5746` n `1013`
- 24h: commodity avg `0.6493` n `13`; crypto_alt avg `-2.5015` n `235`; crypto_major avg `-3.4964` n `8`; equity avg `-2.7403` n `150`; fx avg `0.058` n `6`; index avg `-0.3525` n `26`; metal avg `0.0054` n `20`; unknown avg `6.3189` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
