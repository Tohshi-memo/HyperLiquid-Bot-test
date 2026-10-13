# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T15:07:31.857832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.166` n `235`; crypto_major avg `-0.0966` n `8`; equity avg `0.0169` n `151`; fx avg `0.0019` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0378` n `20`; unknown avg `0.8695` n `1133`
- 1h: commodity avg `-0.0636` n `13`; crypto_alt avg `-0.0606` n `235`; crypto_major avg `0.0334` n `8`; equity avg `-0.225` n `151`; fx avg `0.0002` n `6`; index avg `-0.0491` n `26`; metal avg `-0.0614` n `20`; unknown avg `0.6862` n `1109`
- 4h: commodity avg `0.7362` n `13`; crypto_alt avg `0.8128` n `235`; crypto_major avg `0.7729` n `8`; equity avg `-0.0816` n `151`; fx avg `0.0559` n `6`; index avg `-0.0164` n `26`; metal avg `-0.2749` n `20`; unknown avg `1.2234` n `1095`
- 24h: commodity avg `0.3011` n `13`; crypto_alt avg `-2.0307` n `235`; crypto_major avg `-0.6041` n `8`; equity avg `-1.5169` n `151`; fx avg `0.1224` n `6`; index avg `-0.255` n `26`; metal avg `-0.1746` n `20`; unknown avg `1.1378` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1623`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1467`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1376`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
