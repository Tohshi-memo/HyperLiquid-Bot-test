# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T11:07:28.890555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `0.2249` n `238`; crypto_major avg `0.0723` n `8`; equity avg `-0.1222` n `156`; fx avg `-0.0424` n `6`; index avg `0.0007` n `27`; metal avg `0.0666` n `20`; unknown avg `0.2422` n `1255`
- 1h: commodity avg `0.0175` n `13`; crypto_alt avg `0.7423` n `238`; crypto_major avg `0.6773` n `8`; equity avg `-0.2664` n `156`; fx avg `-0.0468` n `6`; index avg `-0.0126` n `27`; metal avg `-0.0161` n `20`; unknown avg `1.062` n `1255`
- 4h: commodity avg `0.3009` n `13`; crypto_alt avg `0.4126` n `238`; crypto_major avg `-0.7278` n `8`; equity avg `-1.096` n `156`; fx avg `-0.0032` n `6`; index avg `-0.0907` n `27`; metal avg `-0.0565` n `20`; unknown avg `2.8871` n `1190`
- 24h: commodity avg `0.317` n `13`; crypto_alt avg `-3.4296` n `238`; crypto_major avg `-1.666` n `8`; equity avg `-3.9959` n `156`; fx avg `0.0664` n `6`; index avg `-0.4601` n `27`; metal avg `-0.6927` n `20`; unknown avg `23.9592` n `1034`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
