# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T01:07:26.954933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0922` n `13`; crypto_alt avg `0.1706` n `238`; crypto_major avg `0.0823` n `8`; equity avg `0.0257` n `156`; fx avg `0.0059` n `6`; index avg `0.0001` n `27`; metal avg `-0.0019` n `20`; unknown avg `0.7522` n `1256`
- 1h: commodity avg `-0.0797` n `13`; crypto_alt avg `0.1021` n `238`; crypto_major avg `0.2273` n `8`; equity avg `0.0413` n `156`; fx avg `0.0112` n `6`; index avg `-0.0219` n `27`; metal avg `-0.0006` n `20`; unknown avg `0.9031` n `1208`
- 4h: commodity avg `0.0056` n `13`; crypto_alt avg `0.1482` n `238`; crypto_major avg `0.2622` n `8`; equity avg `0.0123` n `156`; fx avg `0.0175` n `6`; index avg `-0.0174` n `27`; metal avg `0.0164` n `20`; unknown avg `1.5223` n `1084`
- 24h: commodity avg `0.0425` n `13`; crypto_alt avg `-0.7178` n `238`; crypto_major avg `-0.3651` n `8`; equity avg `-0.0731` n `156`; fx avg `0.0111` n `6`; index avg `-0.0912` n `27`; metal avg `0.035` n `20`; unknown avg `1.914` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
