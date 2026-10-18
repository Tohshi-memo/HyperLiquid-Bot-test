# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T03:52:30.971638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.3083` n `237`; crypto_major avg `0.19` n `8`; equity avg `0.1636` n `151`; fx avg `0.0009` n `6`; index avg `0.0121` n `26`; metal avg `0.0064` n `20`; unknown avg `0.1914` n `1193`
- 1h: commodity avg `0.0006` n `13`; crypto_alt avg `0.5642` n `237`; crypto_major avg `0.3853` n `8`; equity avg `0.2385` n `151`; fx avg `-0.0124` n `6`; index avg `0.0215` n `26`; metal avg `0.0152` n `20`; unknown avg `0.3313` n `1191`
- 4h: commodity avg `0.0545` n `13`; crypto_alt avg `0.3241` n `236`; crypto_major avg `0.8687` n `8`; equity avg `0.1115` n `151`; fx avg `-0.0195` n `6`; index avg `0.0256` n `26`; metal avg `0.0257` n `20`; unknown avg `5.9568` n `1185`
- 24h: commodity avg `-0.1094` n `13`; crypto_alt avg `-2.0543` n `236`; crypto_major avg `-0.2708` n `8`; equity avg `-0.7358` n `151`; fx avg `-0.0493` n `6`; index avg `-0.0908` n `26`; metal avg `-0.0629` n `20`; unknown avg `3.7605` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1661`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1372`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1053`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0786`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
