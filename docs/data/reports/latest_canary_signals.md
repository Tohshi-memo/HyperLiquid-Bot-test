# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T00:07:23.773630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.079` n `12`; crypto_alt avg `0.1768` n `232`; crypto_major avg `0.0863` n `8`; equity avg `-0.0249` n `129`; fx avg `0.0332` n `6`; index avg `-0.0278` n `26`; metal avg `0.0833` n `20`; unknown avg `-0.0986` n `791`
- 1h: commodity avg `0.0586` n `12`; crypto_alt avg `0.181` n `232`; crypto_major avg `0.1244` n `8`; equity avg `0.0194` n `129`; fx avg `0.0284` n `6`; index avg `0.0061` n `26`; metal avg `0.1025` n `20`; unknown avg `-0.1586` n `791`
- 4h: commodity avg `0.1476` n `12`; crypto_alt avg `0.2579` n `232`; crypto_major avg `-0.2996` n `8`; equity avg `0.0455` n `129`; fx avg `0.0323` n `6`; index avg `-0.0061` n `26`; metal avg `0.0668` n `20`; unknown avg `0.7395` n `773`
- 24h: commodity avg `0.6319` n `12`; crypto_alt avg `2.3185` n `231`; crypto_major avg `1.9261` n `8`; equity avg `1.5507` n `129`; fx avg `-0.0769` n `6`; index avg `0.2371` n `26`; metal avg `-0.1585` n `20`; unknown avg `0.1902` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
