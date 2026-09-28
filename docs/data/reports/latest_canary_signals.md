# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T21:52:33.801602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0213` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.3043` n `234`; crypto_major avg `-0.2093` n `8`; equity avg `-0.018` n `141`; fx avg `0.0015` n `6`; index avg `-0.0051` n `26`; metal avg `0.0006` n `20`; unknown avg `-0.2456` n `939`
- 1h: commodity avg `0.0659` n `12`; crypto_alt avg `-0.349` n `234`; crypto_major avg `-0.3056` n `8`; equity avg `0.0833` n `141`; fx avg `0.0025` n `6`; index avg `0.016` n `26`; metal avg `0.0228` n `20`; unknown avg `0.0299` n `935`
- 4h: commodity avg `0.3655` n `12`; crypto_alt avg `-1.1894` n `234`; crypto_major avg `-1.0673` n `8`; equity avg `-0.327` n `141`; fx avg `-0.011` n `6`; index avg `-0.046` n `26`; metal avg `-0.2175` n `20`; unknown avg `0.568` n `833`
- 24h: commodity avg `-0.2211` n `12`; crypto_alt avg `-4.3394` n `234`; crypto_major avg `-2.4352` n `8`; equity avg `-3.2972` n `141`; fx avg `0.068` n `6`; index avg `-0.3158` n `26`; metal avg `-1.1445` n `20`; unknown avg `24.5308` n `772`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
