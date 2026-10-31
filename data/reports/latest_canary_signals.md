# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T21:52:22.811736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0099` n `13`; crypto_alt avg `-0.0251` n `238`; crypto_major avg `0.0571` n `8`; equity avg `0.013` n `156`; fx avg `0.0021` n `6`; index avg `-0.0012` n `27`; metal avg `0.004` n `20`; unknown avg `5.2431` n `1238`
- 1h: commodity avg `0.0213` n `13`; crypto_alt avg `0.0266` n `238`; crypto_major avg `0.062` n `8`; equity avg `0.0012` n `156`; fx avg `-0.0021` n `6`; index avg `-0.0026` n `27`; metal avg `0.006` n `20`; unknown avg `4.5893` n `1198`
- 4h: commodity avg `0.0413` n `13`; crypto_alt avg `-0.3267` n `238`; crypto_major avg `-0.1662` n `8`; equity avg `0.0034` n `156`; fx avg `0.0055` n `6`; index avg `-0.0039` n `27`; metal avg `0.0013` n `20`; unknown avg `1.3802` n `1142`
- 24h: commodity avg `-0.0974` n `13`; crypto_alt avg `0.2601` n `238`; crypto_major avg `0.3426` n `8`; equity avg `0.3039` n `156`; fx avg `0.0267` n `6`; index avg `-0.0423` n `27`; metal avg `0.0586` n `20`; unknown avg `0.8143` n `1069`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
