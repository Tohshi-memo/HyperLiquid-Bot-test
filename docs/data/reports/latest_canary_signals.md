# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T23:07:29.774011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.0214` n `230`; crypto_major avg `0.0354` n `8`; equity avg `0.1034` n `94`; fx avg `-0.0008` n `6`; index avg `0.0172` n `25`; metal avg `0.0245` n `20`; unknown avg `0.4912` n `768`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `0.0653` n `230`; crypto_major avg `0.1323` n `8`; equity avg `-0.1079` n `94`; fx avg `-0.0075` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.8361` n `768`
- 4h: commodity avg `0.0634` n `12`; crypto_alt avg `0.0951` n `230`; crypto_major avg `0.0614` n `8`; equity avg `0.0482` n `94`; fx avg `-0.0041` n `6`; index avg `0.0065` n `25`; metal avg `-0.0374` n `20`; unknown avg `-0.0453` n `768`
- 24h: commodity avg `0.0834` n `12`; crypto_alt avg `0.3442` n `230`; crypto_major avg `0.6082` n `8`; equity avg `-0.7093` n `93`; fx avg `0.2221` n `6`; index avg `-0.1815` n `25`; metal avg `0.1789` n `20`; unknown avg `0.1557` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1238`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1149`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1084`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0925`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0879`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `669`, weak_sample_signal
