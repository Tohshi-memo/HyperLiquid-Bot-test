# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T01:07:27.337531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0253` n `13`; crypto_alt avg `0.1678` n `236`; crypto_major avg `0.0715` n `8`; equity avg `0.0611` n `151`; fx avg `0.0183` n `6`; index avg `0.008` n `26`; metal avg `0.0033` n `20`; unknown avg `0.0179` n `1134`
- 1h: commodity avg `0.01` n `13`; crypto_alt avg `0.1339` n `236`; crypto_major avg `0.072` n `8`; equity avg `0.3002` n `151`; fx avg `0.0735` n `6`; index avg `0.0707` n `26`; metal avg `-0.0208` n `20`; unknown avg `0.7576` n `1134`
- 4h: commodity avg `-0.0408` n `13`; crypto_alt avg `0.5179` n `236`; crypto_major avg `0.0356` n `8`; equity avg `0.2611` n `151`; fx avg `0.0806` n `6`; index avg `-0.0018` n `26`; metal avg `-0.1123` n `20`; unknown avg `0.0531` n `1096`
- 24h: commodity avg `-0.1038` n `13`; crypto_alt avg `1.2739` n `236`; crypto_major avg `0.6146` n `8`; equity avg `1.5787` n `151`; fx avg `0.0539` n `6`; index avg `0.2538` n `26`; metal avg `0.1914` n `20`; unknown avg `25.6188` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.0897`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.071`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0611`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0529`, n `666`, weak_sample_signal
