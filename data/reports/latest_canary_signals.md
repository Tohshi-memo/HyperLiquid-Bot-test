# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T17:53:12.397425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `13`; crypto_alt avg `0.2013` n `237`; crypto_major avg `0.1029` n `8`; equity avg `0.0563` n `151`; fx avg `0.0081` n `6`; index avg `0.0087` n `26`; metal avg `0.015` n `20`; unknown avg `-0.2601` n `1193`
- 1h: commodity avg `0.0066` n `13`; crypto_alt avg `0.1308` n `237`; crypto_major avg `0.0526` n `8`; equity avg `0.0449` n `151`; fx avg `-0.0028` n `6`; index avg `0.0358` n `26`; metal avg `0.0312` n `20`; unknown avg `-0.2168` n `1189`
- 4h: commodity avg `-0.1328` n `13`; crypto_alt avg `2.0666` n `237`; crypto_major avg `1.4366` n `8`; equity avg `1.8733` n `151`; fx avg `-0.0029` n `6`; index avg `0.2493` n `26`; metal avg `0.0897` n `20`; unknown avg `0.89` n `1132`
- 24h: commodity avg `-0.5206` n `13`; crypto_alt avg `3.2962` n `237`; crypto_major avg `2.0001` n `8`; equity avg `0.4502` n `151`; fx avg `0.0097` n `6`; index avg `0.0693` n `26`; metal avg `0.0276` n `20`; unknown avg `4.236` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
