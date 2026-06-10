# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T02:52:27.229612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2339` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.2386` n `228`; crypto_major avg `-0.2144` n `8`; equity avg `0.028` n `74`; fx avg `0.02` n `6`; index avg `-0.0106` n `23`; metal avg `-0.1632` n `18`; unknown avg `0.0213` n `547`
- 1h: commodity avg `-0.1562` n `12`; crypto_alt avg `-1.0167` n `228`; crypto_major avg `-1.1077` n `8`; equity avg `-0.5098` n `74`; fx avg `0.0248` n `6`; index avg `-0.1085` n `23`; metal avg `-0.4981` n `18`; unknown avg `-0.3063` n `547`
- 4h: commodity avg `-0.226` n `12`; crypto_alt avg `-0.8243` n `228`; crypto_major avg `-1.2776` n `8`; equity avg `-0.1668` n `74`; fx avg `-0.0027` n `6`; index avg `-0.0437` n `23`; metal avg `-1.1821` n `18`; unknown avg `-0.4701` n `547`
- 24h: commodity avg `-0.5869` n `12`; crypto_alt avg `-0.0636` n `228`; crypto_major avg `-2.7307` n `8`; equity avg `-2.5251` n `74`; fx avg `0.1329` n `6`; index avg `-0.9847` n `23`; metal avg `-2.9564` n `18`; unknown avg `-0.1272` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0406`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.04`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
