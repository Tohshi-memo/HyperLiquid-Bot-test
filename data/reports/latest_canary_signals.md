# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T16:52:42.738066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0851` n `13`; crypto_alt avg `0.3652` n `237`; crypto_major avg `0.3222` n `8`; equity avg `-0.1412` n `151`; fx avg `-0.0052` n `6`; index avg `-0.0411` n `26`; metal avg `-0.0181` n `20`; unknown avg `40.3936` n `1199`
- 1h: commodity avg `0.1294` n `13`; crypto_alt avg `0.8586` n `237`; crypto_major avg `0.6956` n `8`; equity avg `0.1638` n `151`; fx avg `0.0089` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0706` n `20`; unknown avg `7.3345` n `1191`
- 4h: commodity avg `-0.3254` n `13`; crypto_alt avg `2.3367` n `237`; crypto_major avg `1.5805` n `8`; equity avg `1.8148` n `151`; fx avg `0.0357` n `6`; index avg `0.2517` n `26`; metal avg `0.1431` n `20`; unknown avg `2.6333` n `1100`
- 24h: commodity avg `-0.3489` n `13`; crypto_alt avg `2.4635` n `237`; crypto_major avg `1.6435` n `8`; equity avg `-0.0004` n `151`; fx avg `0.0327` n `6`; index avg `-0.0164` n `26`; metal avg `0.028` n `20`; unknown avg `3.7651` n `1044`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
