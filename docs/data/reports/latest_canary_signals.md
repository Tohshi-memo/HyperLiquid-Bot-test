# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T05:07:28.305852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `13`; crypto_alt avg `-0.1709` n `237`; crypto_major avg `-0.0525` n `8`; equity avg `0.0688` n `151`; fx avg `0.0022` n `6`; index avg `0.0082` n `26`; metal avg `0.0029` n `20`; unknown avg `-0.009` n `1191`
- 1h: commodity avg `-0.0605` n `13`; crypto_alt avg `-0.4398` n `237`; crypto_major avg `-0.2587` n `8`; equity avg `0.0615` n `151`; fx avg `0.0035` n `6`; index avg `0.0198` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.1076` n `1191`
- 4h: commodity avg `0.0177` n `13`; crypto_alt avg `-0.6458` n `237`; crypto_major avg `0.0275` n `8`; equity avg `0.0499` n `151`; fx avg `-0.0193` n `6`; index avg `0.0198` n `26`; metal avg `0.0094` n `20`; unknown avg `-0.2395` n `1185`
- 24h: commodity avg `-0.1659` n `13`; crypto_alt avg `-2.8257` n `236`; crypto_major avg `-0.681` n `8`; equity avg `-0.8004` n `151`; fx avg `-0.0423` n `6`; index avg `-0.0786` n `26`; metal avg `-0.0608` n `20`; unknown avg `4.0578` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.169`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1339`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
