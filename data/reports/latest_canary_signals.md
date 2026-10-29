# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T06:52:28.042686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `13`; crypto_alt avg `-0.2074` n `238`; crypto_major avg `-0.1072` n `8`; equity avg `-0.0259` n `155`; fx avg `-0.0095` n `6`; index avg `0.0129` n `27`; metal avg `0.0353` n `20`; unknown avg `19.2686` n `1238`
- 1h: commodity avg `0.0129` n `13`; crypto_alt avg `-0.7628` n `238`; crypto_major avg `-0.4493` n `8`; equity avg `-0.3162` n `155`; fx avg `-0.0136` n `6`; index avg `-0.0274` n `27`; metal avg `-0.0165` n `20`; unknown avg `-0.2473` n `1210`
- 4h: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.0603` n `238`; crypto_major avg `0.2326` n `8`; equity avg `0.2363` n `155`; fx avg `-0.0068` n `6`; index avg `0.1302` n `27`; metal avg `-0.2007` n `20`; unknown avg `0.7149` n `1178`
- 24h: commodity avg `-0.1975` n `13`; crypto_alt avg `-2.3053` n `238`; crypto_major avg `-1.3631` n `8`; equity avg `-1.2745` n `154`; fx avg `0.031` n `6`; index avg `-0.0177` n `27`; metal avg `-0.2472` n `20`; unknown avg `30.187` n `970`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
