# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T05:22:30.016054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.2292` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0264` n `13`; crypto_alt avg `-0.359` n `236`; crypto_major avg `-0.3861` n `8`; equity avg `-0.3522` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0539` n `26`; metal avg `-0.0265` n `20`; unknown avg `1.0512` n `1136`
- 1h: commodity avg `-0.0085` n `13`; crypto_alt avg `-0.164` n `236`; crypto_major avg `-0.0676` n `8`; equity avg `-0.0343` n `151`; fx avg `-0.0159` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0086` n `20`; unknown avg `1.2651` n `1134`
- 4h: commodity avg `-0.0217` n `13`; crypto_alt avg `-2.3119` n `236`; crypto_major avg `-1.2432` n `8`; equity avg `-0.2195` n `151`; fx avg `-0.0007` n `6`; index avg `-0.014` n `26`; metal avg `-0.1272` n `20`; unknown avg `1.1987` n `1128`
- 24h: commodity avg `-0.4014` n `13`; crypto_alt avg `-5.3086` n `236`; crypto_major avg `-3.6893` n `8`; equity avg `-5.783` n `151`; fx avg `0.0829` n `6`; index avg `-0.9605` n `26`; metal avg `-0.742` n `20`; unknown avg `1392.6734` n `890`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0992`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.067`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.062`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
