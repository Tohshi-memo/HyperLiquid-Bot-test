# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T14:22:27.931949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1511` n `13`; crypto_alt avg `0.1026` n `235`; crypto_major avg `-0.0855` n `8`; equity avg `-0.0111` n `144`; fx avg `0.0` n `6`; index avg `-0.0017` n `26`; metal avg `0.0017` n `20`; unknown avg `-0.0388` n `1078`
- 1h: commodity avg `-0.04` n `13`; crypto_alt avg `-0.0773` n `235`; crypto_major avg `-0.1502` n `8`; equity avg `0.0126` n `144`; fx avg `0.0005` n `6`; index avg `0.0013` n `26`; metal avg `0.0041` n `20`; unknown avg `0.1715` n `1076`
- 4h: commodity avg `0.0526` n `13`; crypto_alt avg `-0.1071` n `235`; crypto_major avg `-0.3106` n `8`; equity avg `0.0252` n `144`; fx avg `0.0214` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.2018` n `1070`
- 24h: commodity avg `0.0072` n `13`; crypto_alt avg `1.4019` n `235`; crypto_major avg `0.9577` n `8`; equity avg `0.2704` n `144`; fx avg `0.0154` n `6`; index avg `0.0251` n `26`; metal avg `0.0038` n `20`; unknown avg `-0.086` n `915`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2057`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
