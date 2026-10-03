# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T12:37:25.046411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `-0.1745` n `235`; crypto_major avg `-0.0994` n `8`; equity avg `-0.0028` n `143`; fx avg `0.0` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0028` n `20`; unknown avg `0.2083` n `984`
- 1h: commodity avg `-0.024` n `13`; crypto_alt avg `-0.3831` n `235`; crypto_major avg `0.0251` n `8`; equity avg `0.0094` n `143`; fx avg `-0.0045` n `6`; index avg `0.0002` n `26`; metal avg `-0.008` n `20`; unknown avg `0.4767` n `972`
- 4h: commodity avg `-0.0461` n `13`; crypto_alt avg `0.3466` n `235`; crypto_major avg `0.2019` n `8`; equity avg `0.0315` n `143`; fx avg `-0.0208` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.6995` n `972`
- 24h: commodity avg `0.6121` n `13`; crypto_alt avg `-2.6643` n `235`; crypto_major avg `-2.7518` n `8`; equity avg `-0.3107` n `142`; fx avg `0.063` n `6`; index avg `-0.0518` n `26`; metal avg `-0.5741` n `20`; unknown avg `0.1344` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
