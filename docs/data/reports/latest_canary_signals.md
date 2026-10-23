# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T08:52:28.274776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `0.2303` n `237`; crypto_major avg `0.1489` n `8`; equity avg `-0.0601` n `152`; fx avg `0.0035` n `6`; index avg `-0.0246` n `26`; metal avg `0.0584` n `20`; unknown avg `2.6942` n `1233`
- 1h: commodity avg `-0.0468` n `13`; crypto_alt avg `0.2006` n `237`; crypto_major avg `0.3626` n `8`; equity avg `0.4682` n `152`; fx avg `-0.0144` n `6`; index avg `0.0246` n `26`; metal avg `0.0584` n `20`; unknown avg `0.8827` n `1165`
- 4h: commodity avg `0.0221` n `13`; crypto_alt avg `0.5771` n `237`; crypto_major avg `0.6757` n `8`; equity avg `1.4848` n `152`; fx avg `-0.0366` n `6`; index avg `0.0806` n `26`; metal avg `0.1273` n `20`; unknown avg `0.6745` n `1148`
- 24h: commodity avg `0.1373` n `13`; crypto_alt avg `0.5675` n `237`; crypto_major avg `0.6581` n `8`; equity avg `-0.5386` n `152`; fx avg `-0.0717` n `6`; index avg `-0.0512` n `26`; metal avg `-0.3695` n `20`; unknown avg `53.8784` n `872`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1813`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
