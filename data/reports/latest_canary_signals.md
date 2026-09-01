# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T16:37:31.520542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0427` n `12`; crypto_alt avg `-0.2076` n `232`; crypto_major avg `-0.1025` n `8`; equity avg `-0.1839` n `131`; fx avg `-0.0078` n `6`; index avg `-0.0483` n `26`; metal avg `-0.0391` n `20`; unknown avg `-0.2926` n `793`
- 1h: commodity avg `0.3257` n `12`; crypto_alt avg `-0.8363` n `232`; crypto_major avg `-0.7311` n `8`; equity avg `-0.4792` n `131`; fx avg `0.0043` n `6`; index avg `-0.1134` n `26`; metal avg `-0.092` n `20`; unknown avg `-0.533` n `790`
- 4h: commodity avg `0.3972` n `12`; crypto_alt avg `-0.2006` n `232`; crypto_major avg `-0.4457` n `8`; equity avg `-0.3222` n `130`; fx avg `-0.0374` n `6`; index avg `-0.0183` n `26`; metal avg `-0.033` n `20`; unknown avg `-0.34` n `790`
- 24h: commodity avg `0.6548` n `12`; crypto_alt avg `0.3275` n `232`; crypto_major avg `-0.9351` n `8`; equity avg `-1.4318` n `130`; fx avg `0.0356` n `6`; index avg `-0.2264` n `26`; metal avg `-0.5749` n `20`; unknown avg `-0.02` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0349`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0333`, n `668`, weak_sample_signal
