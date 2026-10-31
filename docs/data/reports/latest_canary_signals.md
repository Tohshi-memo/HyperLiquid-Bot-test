# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T02:07:28.321137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `13`; crypto_alt avg `-0.2021` n `238`; crypto_major avg `-0.0514` n `8`; equity avg `-0.0559` n `156`; fx avg `0.0063` n `6`; index avg `-0.0061` n `27`; metal avg `-0.0142` n `20`; unknown avg `0.0212` n `1256`
- 1h: commodity avg `0.0048` n `13`; crypto_alt avg `-0.4837` n `238`; crypto_major avg `-0.246` n `8`; equity avg `-0.1289` n `156`; fx avg `0.0057` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0157` n `20`; unknown avg `-0.291` n `1256`
- 4h: commodity avg `-0.1358` n `13`; crypto_alt avg `0.473` n `238`; crypto_major avg `0.5525` n `8`; equity avg `0.173` n `156`; fx avg `0.0281` n `6`; index avg `0.0107` n `27`; metal avg `0.0002` n `20`; unknown avg `-0.0252` n `1249`
- 24h: commodity avg `-0.3484` n `13`; crypto_alt avg `4.7188` n `238`; crypto_major avg `1.6145` n `8`; equity avg `-1.6471` n `156`; fx avg `-0.1036` n `6`; index avg `-0.0417` n `27`; metal avg `-0.7206` n `20`; unknown avg `-0.8731` n `1018`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
