# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T03:22:39.863629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0387` n `13`; crypto_alt avg `0.0982` n `238`; crypto_major avg `0.0613` n `8`; equity avg `-0.0094` n `156`; fx avg `-0.0035` n `6`; index avg `-0.0167` n `27`; metal avg `0.0039` n `20`; unknown avg `-0.0408` n `1256`
- 1h: commodity avg `-0.0079` n `13`; crypto_alt avg `0.0529` n `238`; crypto_major avg `-0.0576` n `8`; equity avg `0.0278` n `156`; fx avg `-0.0082` n `6`; index avg `-0.0209` n `27`; metal avg `-0.0035` n `20`; unknown avg `-0.1039` n `1244`
- 4h: commodity avg `0.0689` n `13`; crypto_alt avg `0.039` n `238`; crypto_major avg `0.3517` n `8`; equity avg `0.056` n `156`; fx avg `0.0084` n `6`; index avg `-0.0256` n `27`; metal avg `0.0026` n `20`; unknown avg `-0.2623` n `1236`
- 24h: commodity avg `-0.0234` n `13`; crypto_alt avg `3.6529` n `238`; crypto_major avg `0.4457` n `8`; equity avg `-2.1215` n `156`; fx avg `-0.0958` n `6`; index avg `-0.1094` n `27`; metal avg `-0.617` n `20`; unknown avg `-0.617` n `1008`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
