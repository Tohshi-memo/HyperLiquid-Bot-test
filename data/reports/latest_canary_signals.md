# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T23:07:38.731233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `13`; crypto_alt avg `0.0878` n `238`; crypto_major avg `0.0737` n `8`; equity avg `-0.0026` n `156`; fx avg `-0.0093` n `6`; index avg `0.007` n `27`; metal avg `0.0002` n `20`; unknown avg `0.1455` n `1240`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `-0.3219` n `238`; crypto_major avg `-0.3436` n `8`; equity avg `-0.0825` n `156`; fx avg `0.0018` n `6`; index avg `-0.0011` n `27`; metal avg `0.0016` n `20`; unknown avg `0.6593` n `1226`
- 4h: commodity avg `0.0333` n `13`; crypto_alt avg `-0.4618` n `238`; crypto_major avg `-0.3681` n `8`; equity avg `-0.0818` n `156`; fx avg `0.0069` n `6`; index avg `0.0027` n `27`; metal avg `0.01` n `20`; unknown avg `2.0705` n `1090`
- 24h: commodity avg `-0.039` n `13`; crypto_alt avg `-0.568` n `238`; crypto_major avg `-0.1818` n `8`; equity avg `0.1047` n `156`; fx avg `0.0225` n `6`; index avg `-0.0493` n `27`; metal avg `0.0463` n `20`; unknown avg `1.2734` n `1029`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
