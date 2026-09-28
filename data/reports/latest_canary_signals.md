# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T22:07:28.316477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4965` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0822` n `12`; crypto_alt avg `-0.4281` n `234`; crypto_major avg `-0.4311` n `8`; equity avg `-0.041` n `141`; fx avg `0.0113` n `6`; index avg `0.0032` n `26`; metal avg `0.0546` n `20`; unknown avg `-0.0496` n `937`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `-1.0737` n `234`; crypto_major avg `-0.8913` n `8`; equity avg `-0.0306` n `141`; fx avg `0.0007` n `6`; index avg `0.0039` n `26`; metal avg `0.0553` n `20`; unknown avg `0.524` n `937`
- 4h: commodity avg `0.294` n `12`; crypto_alt avg `-1.8351` n `234`; crypto_major avg `-1.5342` n `8`; equity avg `-0.4181` n `141`; fx avg `0.0053` n `6`; index avg `-0.0377` n `26`; metal avg `-0.1458` n `20`; unknown avg `0.3817` n `833`
- 24h: commodity avg `0.0831` n `12`; crypto_alt avg `-4.1314` n `234`; crypto_major avg `-2.386` n `8`; equity avg `-3.1456` n `141`; fx avg `0.0684` n `6`; index avg `-0.2508` n `26`; metal avg `-0.9998` n `20`; unknown avg `29.4474` n `780`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
