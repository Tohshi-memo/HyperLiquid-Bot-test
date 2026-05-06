# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T22:51:56.564967+00:00`
- Correlation status: `ready`
- Asset price records: `495`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.69` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0559` n `12`; crypto_alt avg `-0.0067` n `228`; crypto_major avg `-0.0493` n `8`; equity avg `0.0546` n `65`; fx avg `-0.0008` n `4`; index avg `0.03` n `23`; metal avg `-0.005` n `18`; unknown avg `-0.0708` n `356`
- 1h: commodity avg `-0.1233` n `12`; crypto_alt avg `-0.604` n `228`; crypto_major avg `-0.4007` n `8`; equity avg `0.2663` n `65`; fx avg `-0.0053` n `4`; index avg `-0.0045` n `23`; metal avg `0.0213` n `18`; unknown avg `-0.0312` n `356`
- 4h: commodity avg `0.2875` n `12`; crypto_alt avg `0.1353` n `228`; crypto_major avg `-0.0722` n `8`; equity avg `0.0799` n `65`; fx avg `-0.0081` n `4`; index avg `0.0821` n `23`; metal avg `0.2821` n `18`; unknown avg `0.0725` n `356`
- 24h: commodity avg `-2.2615` n `7`; crypto_alt avg `2.249` n `223`; crypto_major avg `0.1517` n `7`; equity avg `1.9031` n `47`; fx avg `-0.6118` n `4`; index avg `1.44` n `6`; metal avg `3.639` n `7`; unknown avg `3.375` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `491`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `491`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0874`, n `487`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0841`, n `487`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `487`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0756`, n `487`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0745`, n `487`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `491`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0654`, n `491`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `487`, weak_sample_signal
