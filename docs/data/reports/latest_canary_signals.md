# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T03:07:30.456089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.0445` n `235`; crypto_major avg `-0.0233` n `8`; equity avg `0.0023` n `143`; fx avg `0.0007` n `6`; index avg `0.0009` n `26`; metal avg `0.006` n `20`; unknown avg `-0.1175` n `1077`
- 1h: commodity avg `-0.0403` n `13`; crypto_alt avg `-0.0099` n `235`; crypto_major avg `-0.0575` n `8`; equity avg `0.0172` n `143`; fx avg `0.0007` n `6`; index avg `-0.0011` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.2087` n `1077`
- 4h: commodity avg `-0.0422` n `13`; crypto_alt avg `0.0554` n `235`; crypto_major avg `0.0643` n `8`; equity avg `-0.0328` n `143`; fx avg `-0.0118` n `6`; index avg `-0.01` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.108` n `1071`
- 24h: commodity avg `0.1171` n `13`; crypto_alt avg `1.3879` n `235`; crypto_major avg `0.6934` n `8`; equity avg `0.1684` n `143`; fx avg `-0.0277` n `6`; index avg `0.0081` n `26`; metal avg `0.0076` n `20`; unknown avg `0.0665` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
