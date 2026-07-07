# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T21:07:27.949784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0393` n `12`; crypto_alt avg `0.2498` n `229`; crypto_major avg `0.2678` n `8`; equity avg `0.0486` n `91`; fx avg `0.0117` n `6`; index avg `0.003` n `25`; metal avg `0.0142` n `20`; unknown avg `-0.0402` n `763`
- 1h: commodity avg `0.126` n `12`; crypto_alt avg `-0.0318` n `229`; crypto_major avg `0.0787` n `8`; equity avg `0.0644` n `91`; fx avg `0.0183` n `6`; index avg `-0.0126` n `25`; metal avg `-0.0968` n `20`; unknown avg `-0.1047` n `763`
- 4h: commodity avg `0.421` n `12`; crypto_alt avg `-1.3367` n `229`; crypto_major avg `-0.958` n `8`; equity avg `-0.6359` n `91`; fx avg `0.0029` n `6`; index avg `-0.0911` n `25`; metal avg `-0.4232` n `20`; unknown avg `0.2159` n `761`
- 24h: commodity avg `0.9603` n `12`; crypto_alt avg `-1.9539` n `229`; crypto_major avg `-1.1154` n `8`; equity avg `-3.1673` n `91`; fx avg `-0.2318` n `6`; index avg `-0.6108` n `25`; metal avg `-0.5864` n `20`; unknown avg `-0.2186` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
