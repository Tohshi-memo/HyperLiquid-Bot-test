# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T03:37:28.092090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `13`; crypto_alt avg `0.1076` n `238`; crypto_major avg `0.0169` n `8`; equity avg `0.0407` n `156`; fx avg `-0.0031` n `6`; index avg `0.0013` n `27`; metal avg `0.0042` n `20`; unknown avg `0.8067` n `1260`
- 1h: commodity avg `0.0938` n `13`; crypto_alt avg `0.4316` n `238`; crypto_major avg `0.1579` n `8`; equity avg `0.1073` n `156`; fx avg `-0.0025` n `6`; index avg `0.0239` n `27`; metal avg `0.004` n `20`; unknown avg `1.2407` n `1252`
- 4h: commodity avg `0.0645` n `13`; crypto_alt avg `0.2055` n `238`; crypto_major avg `0.1645` n `8`; equity avg `0.1259` n `156`; fx avg `-0.002` n `6`; index avg `0.0035` n `27`; metal avg `0.0097` n `20`; unknown avg `0.901` n `1198`
- 24h: commodity avg `-0.0264` n `13`; crypto_alt avg `-0.1439` n `238`; crypto_major avg `-0.1374` n `8`; equity avg `0.1076` n `156`; fx avg `0.0082` n `6`; index avg `-0.0211` n `27`; metal avg `0.0562` n `20`; unknown avg `2.0045` n `1000`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
