# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T19:37:37.345362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `0.2917` n `237`; crypto_major avg `0.2169` n `8`; equity avg `0.0337` n `151`; fx avg `-0.0073` n `6`; index avg `-0.001` n `26`; metal avg `0.002` n `20`; unknown avg `76.4764` n `1197`
- 1h: commodity avg `0.0831` n `13`; crypto_alt avg `0.0137` n `237`; crypto_major avg `0.0783` n `8`; equity avg `0.1141` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0356` n `20`; unknown avg `44.4745` n `1195`
- 4h: commodity avg `0.297` n `13`; crypto_alt avg `0.4359` n `237`; crypto_major avg `0.4247` n `8`; equity avg `0.0139` n `151`; fx avg `0.0049` n `6`; index avg `-0.02` n `26`; metal avg `-0.0685` n `20`; unknown avg `8.6488` n `1175`
- 24h: commodity avg `-0.0554` n `13`; crypto_alt avg `2.3922` n `237`; crypto_major avg `1.489` n `8`; equity avg `-0.3239` n `151`; fx avg `0.0265` n `6`; index avg `-0.0779` n `26`; metal avg `-0.0459` n `20`; unknown avg `6.4602` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
