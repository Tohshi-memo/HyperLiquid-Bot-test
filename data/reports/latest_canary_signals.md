# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T20:52:26.576395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `13`; crypto_alt avg `0.1037` n `236`; crypto_major avg `0.0878` n `8`; equity avg `0.0035` n `151`; fx avg `-0.0026` n `6`; index avg `-0.0083` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.0117` n `1193`
- 1h: commodity avg `0.0074` n `13`; crypto_alt avg `-0.0741` n `236`; crypto_major avg `0.1064` n `8`; equity avg `-0.0445` n `151`; fx avg `-0.002` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.0699` n `1177`
- 4h: commodity avg `-0.006` n `13`; crypto_alt avg `1.0206` n `236`; crypto_major avg `0.7215` n `8`; equity avg `0.122` n `151`; fx avg `-0.0106` n `6`; index avg `0.0009` n `26`; metal avg `0.0132` n `20`; unknown avg `3.0244` n `1113`
- 24h: commodity avg `0.0441` n `13`; crypto_alt avg `-0.9973` n `236`; crypto_major avg `-0.1341` n `8`; equity avg `-0.2693` n `151`; fx avg `-0.0318` n `6`; index avg `-0.0294` n `26`; metal avg `-0.024` n `20`; unknown avg `4.4871` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1711`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1482`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
