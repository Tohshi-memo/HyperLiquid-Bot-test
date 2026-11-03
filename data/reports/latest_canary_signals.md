# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T05:37:25.020345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `-0.2187` n `239`; crypto_major avg `-0.244` n `8`; equity avg `-0.1817` n `157`; fx avg `0.0128` n `6`; index avg `-0.0232` n `27`; metal avg `-0.0708` n `20`; unknown avg `0.4552` n `1260`
- 1h: commodity avg `0.0797` n `13`; crypto_alt avg `-0.4469` n `239`; crypto_major avg `-0.4245` n `8`; equity avg `-0.353` n `157`; fx avg `0.0334` n `6`; index avg `-0.0217` n `27`; metal avg `-0.0756` n `20`; unknown avg `0.241` n `1248`
- 4h: commodity avg `0.1913` n `13`; crypto_alt avg `-0.4998` n `239`; crypto_major avg `-0.5269` n `8`; equity avg `-0.9376` n `157`; fx avg `-0.008` n `6`; index avg `-0.1165` n `27`; metal avg `-0.3789` n `20`; unknown avg `-0.0566` n `1188`
- 24h: commodity avg `-0.7114` n `13`; crypto_alt avg `-3.221` n `238`; crypto_major avg `-2.2659` n `8`; equity avg `-4.6441` n `157`; fx avg `0.0324` n `6`; index avg `-0.404` n `27`; metal avg `-0.4041` n `20`; unknown avg `7.9313` n `955`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
