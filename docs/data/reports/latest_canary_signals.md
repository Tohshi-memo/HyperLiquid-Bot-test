# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T23:22:27.251927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `0.021` n `238`; crypto_major avg `-0.0104` n `8`; equity avg `0.0122` n `156`; fx avg `0.0018` n `6`; index avg `0.0079` n `27`; metal avg `-0.0029` n `20`; unknown avg `396.3212` n `1262`
- 1h: commodity avg `-0.001` n `13`; crypto_alt avg `-0.1579` n `238`; crypto_major avg `-0.2577` n `8`; equity avg `-0.0468` n `156`; fx avg `-0.0001` n `6`; index avg `0.0123` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.5248` n `1232`
- 4h: commodity avg `0.0268` n `13`; crypto_alt avg `-0.2901` n `238`; crypto_major avg `-0.2732` n `8`; equity avg `-0.0469` n `156`; fx avg `0.0074` n `6`; index avg `0.0069` n `27`; metal avg `0.0076` n `20`; unknown avg `2.43` n `1090`
- 24h: commodity avg `-0.0246` n `13`; crypto_alt avg `-0.5075` n `238`; crypto_major avg `-0.1526` n `8`; equity avg `0.0354` n `156`; fx avg `0.0173` n `6`; index avg `-0.0528` n `27`; metal avg `0.0512` n `20`; unknown avg `1.0856` n `1030`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
