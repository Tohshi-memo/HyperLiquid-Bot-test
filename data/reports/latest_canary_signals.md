# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T01:00:12.078160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1198` n `13`; crypto_alt avg `-0.2235` n `237`; crypto_major avg `-0.4278` n `8`; equity avg `-0.0959` n `151`; fx avg `0.0106` n `6`; index avg `-0.0063` n `26`; metal avg `-0.1982` n `20`; unknown avg `4.539` n `1193`
- 1h: commodity avg `0.1198` n `13`; crypto_alt avg `-0.2235` n `237`; crypto_major avg `-0.4278` n `8`; equity avg `-0.0959` n `151`; fx avg `0.0106` n `6`; index avg `-0.0063` n `26`; metal avg `-0.1982` n `20`; unknown avg `4.539` n `1193`
- 4h: commodity avg `0.1982` n `13`; crypto_alt avg `-0.853` n `237`; crypto_major avg `-0.9413` n `8`; equity avg `-1.0803` n `151`; fx avg `-0.0129` n `6`; index avg `-0.1656` n `26`; metal avg `-0.2069` n `20`; unknown avg `2.9726` n `1042`
- 24h: commodity avg `-0.5532` n `13`; crypto_alt avg `1.5639` n `237`; crypto_major avg `0.7735` n `8`; equity avg `-0.712` n `151`; fx avg `0.0091` n `6`; index avg `-0.0356` n `26`; metal avg `-0.2565` n `20`; unknown avg `118.5018` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.166`, n `671`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1446`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `671`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1209`, n `671`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1177`, n `671`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `671`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `671`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `671`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0888`, n `671`, weak_sample_signal
