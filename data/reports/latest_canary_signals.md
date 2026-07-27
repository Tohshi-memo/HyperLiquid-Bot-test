# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T18:22:31.985478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `-0.1971` n `230`; crypto_major avg `-0.2869` n `8`; equity avg `-0.1673` n `102`; fx avg `0.005` n `6`; index avg `-0.0246` n `25`; metal avg `-0.0556` n `20`; unknown avg `-0.1535` n `774`
- 1h: commodity avg `-0.0658` n `12`; crypto_alt avg `-0.3737` n `230`; crypto_major avg `-0.5554` n `8`; equity avg `0.0605` n `102`; fx avg `0.0233` n `6`; index avg `0.0457` n `25`; metal avg `-0.0417` n `20`; unknown avg `-0.3655` n `774`
- 4h: commodity avg `-0.3197` n `12`; crypto_alt avg `-0.7947` n `230`; crypto_major avg `-0.7088` n `8`; equity avg `-0.5378` n `102`; fx avg `-0.0656` n `6`; index avg `-0.2002` n `25`; metal avg `-0.0169` n `20`; unknown avg `-0.6312` n `774`
- 24h: commodity avg `-0.8042` n `12`; crypto_alt avg `-1.2109` n `230`; crypto_major avg `-0.6166` n `8`; equity avg `-1.8286` n `102`; fx avg `-0.0038` n `6`; index avg `-0.5023` n `25`; metal avg `0.1363` n `20`; unknown avg `-0.4902` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
