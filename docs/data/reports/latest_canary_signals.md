# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T09:37:36.352432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `13`; crypto_alt avg `-0.3125` n `238`; crypto_major avg `-0.2169` n `8`; equity avg `-0.2048` n `155`; fx avg `0.0083` n `6`; index avg `0.0051` n `27`; metal avg `-0.0516` n `20`; unknown avg `-0.1603` n `1236`
- 1h: commodity avg `0.0871` n `13`; crypto_alt avg `0.1347` n `238`; crypto_major avg `-0.0772` n `8`; equity avg `0.1064` n `155`; fx avg `-0.004` n `6`; index avg `0.0969` n `27`; metal avg `-0.1195` n `20`; unknown avg `-0.119` n `1226`
- 4h: commodity avg `0.1296` n `13`; crypto_alt avg `-0.9637` n `238`; crypto_major avg `-0.5987` n `8`; equity avg `-0.5982` n `155`; fx avg `-0.0025` n `6`; index avg `-0.0405` n `27`; metal avg `-0.2675` n `20`; unknown avg `-0.4557` n `1192`
- 24h: commodity avg `-0.0179` n `13`; crypto_alt avg `-2.6973` n `238`; crypto_major avg `-1.9433` n `8`; equity avg `-1.3772` n `155`; fx avg `0.0171` n `6`; index avg `0.0167` n `27`; metal avg `-0.4995` n `20`; unknown avg `25.7802` n `1000`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
