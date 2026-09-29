# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T01:22:32.412889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `-0.493` n `234`; crypto_major avg `-0.2095` n `8`; equity avg `-0.1718` n `141`; fx avg `0.0205` n `6`; index avg `-0.0183` n `26`; metal avg `0.0053` n `20`; unknown avg `0.2097` n `963`
- 1h: commodity avg `0.0901` n `12`; crypto_alt avg `-1.0506` n `234`; crypto_major avg `-0.6036` n `8`; equity avg `-0.4478` n `141`; fx avg `-0.0099` n `6`; index avg `-0.0524` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.6382` n `961`
- 4h: commodity avg `0.0634` n `12`; crypto_alt avg `-0.598` n `234`; crypto_major avg `-0.6339` n `8`; equity avg `-0.4913` n `141`; fx avg `-0.0243` n `6`; index avg `-0.0792` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.3332` n `931`
- 24h: commodity avg `0.1015` n `12`; crypto_alt avg `-4.1516` n `234`; crypto_major avg `-2.2971` n `8`; equity avg `-2.8611` n `141`; fx avg `-0.0559` n `6`; index avg `-0.2559` n `26`; metal avg `-0.6371` n `20`; unknown avg `153.1581` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
