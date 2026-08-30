# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T04:37:26.954015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.1203` n `231`; crypto_major avg `-0.0558` n `8`; equity avg `-0.0133` n `128`; fx avg `-0.0006` n `6`; index avg `-0.008` n `26`; metal avg `0.0008` n `20`; unknown avg `0.0356` n `793`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.3391` n `231`; crypto_major avg `-0.1671` n `8`; equity avg `0.0125` n `128`; fx avg `0.0012` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.3041` n `793`
- 4h: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.2032` n `231`; crypto_major avg `-0.2666` n `8`; equity avg `0.0165` n `128`; fx avg `0.0067` n `6`; index avg `-0.0161` n `26`; metal avg `0.0002` n `20`; unknown avg `-0.403` n `793`
- 24h: commodity avg `-0.0081` n `12`; crypto_alt avg `0.2072` n `231`; crypto_major avg `0.6483` n `8`; equity avg `0.3085` n `128`; fx avg `-0.0145` n `6`; index avg `0.0449` n `26`; metal avg `0.0896` n `20`; unknown avg `0.1416` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
