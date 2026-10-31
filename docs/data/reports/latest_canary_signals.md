# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T07:37:36.400672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `13`; crypto_alt avg `-0.2508` n `238`; crypto_major avg `-0.1342` n `8`; equity avg `-0.0067` n `156`; fx avg `0.0035` n `6`; index avg `0.0064` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.5231` n `1262`
- 1h: commodity avg `-0.0229` n `13`; crypto_alt avg `-0.3038` n `238`; crypto_major avg `-0.1362` n `8`; equity avg `0.0081` n `156`; fx avg `0.0095` n `6`; index avg `-0.0002` n `27`; metal avg `-0.026` n `20`; unknown avg `4.8331` n `1256`
- 4h: commodity avg `-0.0529` n `13`; crypto_alt avg `-0.7211` n `238`; crypto_major avg `-0.4929` n `8`; equity avg `-0.0274` n `156`; fx avg `0.0139` n `6`; index avg `-0.008` n `27`; metal avg `0.0047` n `20`; unknown avg `0.9329` n `1218`
- 24h: commodity avg `-0.1849` n `13`; crypto_alt avg `0.9377` n `238`; crypto_major avg `-1.029` n `8`; equity avg `-2.2764` n `156`; fx avg `-0.0686` n `6`; index avg `-0.2437` n `27`; metal avg `-0.4279` n `20`; unknown avg `4.5522` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
