# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T22:52:34.053811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0039` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.1941` n `234`; crypto_major avg `0.0884` n `8`; equity avg `-0.0089` n `141`; fx avg `0.0036` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.907` n `963`
- 1h: commodity avg `-0.0775` n `12`; crypto_alt avg `0.3678` n `234`; crypto_major avg `0.2092` n `8`; equity avg `0.0311` n `141`; fx avg `0.0098` n `6`; index avg `0.0069` n `26`; metal avg `0.0304` n `20`; unknown avg `0.4153` n `937`
- 4h: commodity avg `0.2618` n `12`; crypto_alt avg `-0.9629` n `234`; crypto_major avg `-1.0391` n `8`; equity avg `-0.3535` n `141`; fx avg `0.009` n `6`; index avg `-0.0352` n `26`; metal avg `-0.1538` n `20`; unknown avg `0.6437` n `833`
- 24h: commodity avg `0.0552` n `12`; crypto_alt avg `-3.4057` n `234`; crypto_major avg `-1.6172` n `8`; equity avg `-2.9184` n `141`; fx avg `0.0553` n `6`; index avg `-0.1968` n `26`; metal avg `-0.9359` n `20`; unknown avg `102.5521` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
