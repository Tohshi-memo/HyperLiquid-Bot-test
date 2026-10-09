# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T08:37:31.974371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `13`; crypto_alt avg `-0.0265` n `235`; crypto_major avg `-0.136` n `8`; equity avg `-0.0264` n `150`; fx avg `-0.013` n `6`; index avg `0.0027` n `26`; metal avg `-0.0432` n `20`; unknown avg `-0.0474` n `1078`
- 1h: commodity avg `-0.0872` n `13`; crypto_alt avg `-0.1767` n `235`; crypto_major avg `-0.1829` n `8`; equity avg `0.0867` n `150`; fx avg `0.0018` n `6`; index avg `0.0253` n `26`; metal avg `0.016` n `20`; unknown avg `-0.2012` n `1006`
- 4h: commodity avg `-0.0491` n `13`; crypto_alt avg `0.465` n `235`; crypto_major avg `0.2231` n `8`; equity avg `0.6084` n `150`; fx avg `0.0536` n `6`; index avg `0.0827` n `26`; metal avg `0.1356` n `20`; unknown avg `1.6496` n `988`
- 24h: commodity avg `-0.4137` n `13`; crypto_alt avg `-0.9469` n `235`; crypto_major avg `-1.7938` n `8`; equity avg `-0.4045` n `150`; fx avg `0.1473` n `6`; index avg `0.0548` n `26`; metal avg `0.4829` n `20`; unknown avg `7.1046` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
