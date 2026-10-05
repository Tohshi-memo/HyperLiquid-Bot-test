# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T03:37:32.602988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.65` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0105` n `13`; crypto_alt avg `0.0158` n `235`; crypto_major avg `0.0904` n `8`; equity avg `0.03` n `144`; fx avg `-0.0078` n `6`; index avg `-0.0058` n `26`; metal avg `0.0327` n `20`; unknown avg `-0.1131` n `1044`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `-0.5245` n `235`; crypto_major avg `-0.4037` n `8`; equity avg `-0.0988` n `144`; fx avg `-0.0564` n `6`; index avg `-0.039` n `26`; metal avg `-0.0675` n `20`; unknown avg `0.2719` n `1030`
- 4h: commodity avg `-0.1391` n `13`; crypto_alt avg `-0.0039` n `235`; crypto_major avg `-0.0994` n `8`; equity avg `0.0561` n `144`; fx avg `-0.1105` n `6`; index avg `-0.0324` n `26`; metal avg `0.0282` n `20`; unknown avg `0.5307` n `994`
- 24h: commodity avg `-0.3239` n `13`; crypto_alt avg `0.9426` n `235`; crypto_major avg `1.3369` n `8`; equity avg `0.4327` n `144`; fx avg `-0.1089` n `6`; index avg `-0.0167` n `26`; metal avg `0.1025` n `20`; unknown avg `0.3545` n `906`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
