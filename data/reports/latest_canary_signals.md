# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T09:07:32.945665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1328` n `12`; crypto_alt avg `-0.1446` n `230`; crypto_major avg `-0.049` n `8`; equity avg `-0.0833` n `102`; fx avg `0.002` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0064` n `20`; unknown avg `-0.0433` n `774`
- 1h: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.1789` n `230`; crypto_major avg `-0.1133` n `8`; equity avg `0.2798` n `102`; fx avg `0.0202` n `6`; index avg `0.0607` n `25`; metal avg `-0.0527` n `20`; unknown avg `0.0091` n `774`
- 4h: commodity avg `-0.235` n `12`; crypto_alt avg `-0.3226` n `230`; crypto_major avg `-0.368` n `8`; equity avg `-0.0909` n `102`; fx avg `-0.0116` n `6`; index avg `-0.0081` n `25`; metal avg `0.0332` n `20`; unknown avg `-0.0248` n `758`
- 24h: commodity avg `-0.5472` n `12`; crypto_alt avg `-3.4735` n `230`; crypto_major avg `-3.4663` n `8`; equity avg `-3.9728` n `102`; fx avg `-0.1509` n `6`; index avg `-0.8433` n `25`; metal avg `-0.4728` n `20`; unknown avg `1158.3433` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
