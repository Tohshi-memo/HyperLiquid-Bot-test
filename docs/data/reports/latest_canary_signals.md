# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T04:37:26.683043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `13`; crypto_alt avg `-0.0389` n `238`; crypto_major avg `0.0006` n `8`; equity avg `0.0301` n `156`; fx avg `-0.0105` n `6`; index avg `0.005` n `27`; metal avg `0.002` n `20`; unknown avg `-0.0899` n `1262`
- 1h: commodity avg `0.0025` n `13`; crypto_alt avg `-0.0028` n `238`; crypto_major avg `-0.0125` n `8`; equity avg `0.0609` n `156`; fx avg `-0.0096` n `6`; index avg `0.0066` n `27`; metal avg `-0.0002` n `20`; unknown avg `0.4238` n `1246`
- 4h: commodity avg `0.0001` n `13`; crypto_alt avg `0.0989` n `238`; crypto_major avg `-0.0911` n `8`; equity avg `0.1738` n `156`; fx avg `-0.0101` n `6`; index avg `0.0329` n `27`; metal avg `0.0081` n `20`; unknown avg `2.315` n `1240`
- 24h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.1526` n `238`; crypto_major avg `0.2236` n `8`; equity avg `0.2104` n `156`; fx avg `-0.0092` n `6`; index avg `0.0027` n `27`; metal avg `0.0611` n `20`; unknown avg `2.8791` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
