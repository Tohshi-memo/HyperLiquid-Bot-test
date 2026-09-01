# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T17:07:30.424673+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `-0.0784` n `232`; crypto_major avg `-0.097` n `8`; equity avg `-0.0806` n `131`; fx avg `-0.0063` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0843` n `20`; unknown avg `-0.2636` n `791`
- 1h: commodity avg `0.3025` n `12`; crypto_alt avg `-0.6893` n `232`; crypto_major avg `-0.5475` n `8`; equity avg `-0.5659` n `131`; fx avg `0.0012` n `6`; index avg `-0.1363` n `26`; metal avg `-0.1987` n `20`; unknown avg `-0.2595` n `791`
- 4h: commodity avg `0.3895` n `12`; crypto_alt avg `0.0165` n `232`; crypto_major avg `-0.3572` n `8`; equity avg `-0.2613` n `131`; fx avg `-0.0334` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0279` n `20`; unknown avg `-0.2176` n `790`
- 24h: commodity avg `0.6198` n `12`; crypto_alt avg `0.1543` n `232`; crypto_major avg `-1.1972` n `8`; equity avg `-1.4757` n `130`; fx avg `0.0348` n `6`; index avg `-0.2426` n `26`; metal avg `-0.6181` n `20`; unknown avg `-0.231` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0405`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0347`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0346`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0343`, n `668`, weak_sample_signal
