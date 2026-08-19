# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T06:07:37.737473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `-0.1689` n `230`; crypto_major avg `-0.1352` n `8`; equity avg `-0.299` n `120`; fx avg `-0.0144` n `6`; index avg `-0.0281` n `25`; metal avg `-0.026` n `20`; unknown avg `-0.02` n `757`
- 1h: commodity avg `0.0528` n `12`; crypto_alt avg `-0.162` n `230`; crypto_major avg `-0.2302` n `8`; equity avg `-0.4911` n `120`; fx avg `-0.0311` n `6`; index avg `-0.0648` n `25`; metal avg `-0.0406` n `20`; unknown avg `-0.0568` n `757`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.2173` n `230`; crypto_major avg `-0.14` n `8`; equity avg `-1.0697` n `120`; fx avg `-0.1128` n `6`; index avg `-0.1108` n `25`; metal avg `-0.1389` n `20`; unknown avg `-0.1741` n `757`
- 24h: commodity avg `0.2644` n `12`; crypto_alt avg `0.4916` n `230`; crypto_major avg `0.1396` n `8`; equity avg `-3.3208` n `120`; fx avg `-0.1779` n `6`; index avg `-0.4432` n `25`; metal avg `-0.6353` n `20`; unknown avg `-0.2379` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
