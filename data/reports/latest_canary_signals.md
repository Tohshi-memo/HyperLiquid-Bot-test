# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T07:52:32.817501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0564` n `13`; crypto_alt avg `0.2153` n `235`; crypto_major avg `0.1196` n `8`; equity avg `0.0885` n `144`; fx avg `0.0095` n `6`; index avg `0.0251` n `26`; metal avg `0.1062` n `20`; unknown avg `3.2001` n `1079`
- 1h: commodity avg `-0.029` n `13`; crypto_alt avg `0.6286` n `235`; crypto_major avg `0.4202` n `8`; equity avg `0.108` n `144`; fx avg `0.0137` n `6`; index avg `0.0326` n `26`; metal avg `0.1283` n `20`; unknown avg `2.6459` n `1077`
- 4h: commodity avg `0.0325` n `13`; crypto_alt avg `0.8316` n `235`; crypto_major avg `0.607` n `8`; equity avg `-0.0301` n `144`; fx avg `0.0405` n `6`; index avg `-0.0014` n `26`; metal avg `0.1637` n `20`; unknown avg `2.4417` n `1033`
- 24h: commodity avg `-0.2919` n `13`; crypto_alt avg `1.1011` n `235`; crypto_major avg `1.5407` n `8`; equity avg `0.3643` n `144`; fx avg `-0.0649` n `6`; index avg `-0.0144` n `26`; metal avg `0.2775` n `20`; unknown avg `0.104` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1983`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
