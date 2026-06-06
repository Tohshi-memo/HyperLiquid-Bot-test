# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T12:52:23.336246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0768` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `0.7297` n `228`; crypto_major avg `0.8027` n `8`; equity avg `0.2234` n `74`; fx avg `-0.0019` n `6`; index avg `0.04` n `23`; metal avg `0.0653` n `18`; unknown avg `0.0627` n `425`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `0.353` n `228`; crypto_major avg `0.378` n `8`; equity avg `0.4802` n `74`; fx avg `-0.004` n `6`; index avg `0.3762` n `23`; metal avg `0.0493` n `18`; unknown avg `-0.0451` n `423`
- 4h: commodity avg `0.0797` n `12`; crypto_alt avg `-0.4976` n `228`; crypto_major avg `-0.6665` n `8`; equity avg `0.7092` n `74`; fx avg `0.0063` n `6`; index avg `0.4103` n `23`; metal avg `0.0272` n `18`; unknown avg `-0.1456` n `421`
- 24h: commodity avg `-0.9393` n `12`; crypto_alt avg `-2.4516` n `228`; crypto_major avg `-2.4628` n `8`; equity avg `-5.8554` n `74`; fx avg `-0.229` n `6`; index avg `-3.4944` n `23`; metal avg `-3.839` n `18`; unknown avg `0.4849` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
