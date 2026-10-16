# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T13:37:33.417337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0527` n `13`; crypto_alt avg `-0.2298` n `236`; crypto_major avg `-0.25` n `8`; equity avg `-0.8064` n `151`; fx avg `0.0164` n `6`; index avg `-0.1039` n `26`; metal avg `0.1213` n `20`; unknown avg `96.3313` n `1136`
- 1h: commodity avg `0.024` n `13`; crypto_alt avg `-0.7293` n `236`; crypto_major avg `-0.6363` n `8`; equity avg `-0.9457` n `151`; fx avg `0.0192` n `6`; index avg `-0.1282` n `26`; metal avg `-0.0026` n `20`; unknown avg `37.2197` n `1134`
- 4h: commodity avg `-0.026` n `13`; crypto_alt avg `-0.4333` n `236`; crypto_major avg `-0.5646` n `8`; equity avg `-1.5902` n `151`; fx avg `0.0225` n `6`; index avg `-0.1787` n `26`; metal avg `-0.0305` n `20`; unknown avg `13.6827` n `1128`
- 24h: commodity avg `-0.147` n `13`; crypto_alt avg `4.6499` n `236`; crypto_major avg `2.5883` n `8`; equity avg `2.0936` n `151`; fx avg `0.048` n `6`; index avg `0.2191` n `26`; metal avg `0.188` n `20`; unknown avg `25.0593` n `944`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0918`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0786`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
