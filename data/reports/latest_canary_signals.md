# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T03:52:23.014163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `13`; crypto_alt avg `0.1446` n `237`; crypto_major avg `0.2242` n `8`; equity avg `0.1453` n `151`; fx avg `-0.0103` n `6`; index avg `0.0289` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.3716` n `1233`
- 1h: commodity avg `-0.0063` n `13`; crypto_alt avg `0.0567` n `237`; crypto_major avg `0.0803` n `8`; equity avg `0.2069` n `151`; fx avg `-0.0147` n `6`; index avg `0.0519` n `26`; metal avg `-0.0278` n `20`; unknown avg `0.3332` n `1229`
- 4h: commodity avg `0.0247` n `13`; crypto_alt avg `1.4421` n `237`; crypto_major avg `0.9529` n `8`; equity avg `1.3774` n `151`; fx avg `-0.0245` n `6`; index avg `0.1137` n `26`; metal avg `-0.0063` n `20`; unknown avg `0.7179` n `1223`
- 24h: commodity avg `0.3868` n `13`; crypto_alt avg `-1.5412` n `237`; crypto_major avg `-0.763` n `8`; equity avg `-2.6668` n `151`; fx avg `-0.1415` n `6`; index avg `-0.2807` n `26`; metal avg `-0.5229` n `20`; unknown avg `53.256` n `903`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
