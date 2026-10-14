# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T07:07:29.910552+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0564` n `13`; crypto_alt avg `0.1664` n `235`; crypto_major avg `0.1677` n `8`; equity avg `0.1403` n `151`; fx avg `-0.0229` n `6`; index avg `0.0055` n `26`; metal avg `-0.0322` n `20`; unknown avg `0.1434` n `1133`
- 1h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.3343` n `235`; crypto_major avg `0.2369` n `8`; equity avg `0.3301` n `151`; fx avg `-0.0471` n `6`; index avg `0.0973` n `26`; metal avg `-0.0305` n `20`; unknown avg `0.3757` n `1133`
- 4h: commodity avg `-0.0748` n `13`; crypto_alt avg `-0.447` n `235`; crypto_major avg `-0.2255` n `8`; equity avg `-0.6475` n `151`; fx avg `-0.052` n `6`; index avg `-0.0826` n `26`; metal avg `-0.1262` n `20`; unknown avg `0.3888` n `1111`
- 24h: commodity avg `1.0121` n `13`; crypto_alt avg `-0.8749` n `235`; crypto_major avg `-0.2953` n `8`; equity avg `0.2276` n `151`; fx avg `0.0126` n `6`; index avg `0.0597` n `26`; metal avg `-0.4205` n `20`; unknown avg `0.4939` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1552`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1359`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `666`, weak_sample_signal
