# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T06:37:31.297906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4883` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0423` n `12`; crypto_alt avg `0.5269` n `228`; crypto_major avg `0.3978` n `8`; equity avg `0.1949` n `86`; fx avg `0.0029` n `6`; index avg `-0.0767` n `23`; metal avg `-0.1238` n `20`; unknown avg `0.0339` n `716`
- 1h: commodity avg `-0.1392` n `12`; crypto_alt avg `-1.4009` n `228`; crypto_major avg `-1.0045` n `8`; equity avg `-0.5439` n `86`; fx avg `0.0741` n `6`; index avg `-0.2362` n `23`; metal avg `-0.3075` n `20`; unknown avg `-0.4734` n `676`
- 4h: commodity avg `-0.2521` n `12`; crypto_alt avg `-1.8519` n `228`; crypto_major avg `-2.0411` n `8`; equity avg `-2.0068` n `86`; fx avg `0.0462` n `6`; index avg `-0.5528` n `23`; metal avg `-0.6353` n `20`; unknown avg `0.0146` n `676`
- 24h: commodity avg `-0.6249` n `12`; crypto_alt avg `-2.8742` n `228`; crypto_major avg `-2.3519` n `8`; equity avg `-4.1076` n `85`; fx avg `-0.0029` n `6`; index avg `-0.8422` n `23`; metal avg `-1.5175` n `18`; unknown avg `0.6456` n `647`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
