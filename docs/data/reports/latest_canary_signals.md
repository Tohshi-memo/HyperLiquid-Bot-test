# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T07:22:33.685391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.2345` n `238`; crypto_major avg `-0.0876` n `8`; equity avg `-0.0847` n `155`; fx avg `0.0076` n `6`; index avg `-0.0174` n `27`; metal avg `-0.0547` n `20`; unknown avg `0.4334` n `1238`
- 1h: commodity avg `0.0333` n `13`; crypto_alt avg `-0.5495` n `238`; crypto_major avg `-0.1486` n `8`; equity avg `-0.24` n `155`; fx avg `0.0032` n `6`; index avg `-0.0163` n `27`; metal avg `0.0115` n `20`; unknown avg `11.4788` n `1228`
- 4h: commodity avg `0.0027` n `13`; crypto_alt avg `-0.1266` n `238`; crypto_major avg `0.3519` n `8`; equity avg `0.3436` n `155`; fx avg `0.0006` n `6`; index avg `0.1825` n `27`; metal avg `-0.0636` n `20`; unknown avg `0.3152` n `1186`
- 24h: commodity avg `-0.2119` n `13`; crypto_alt avg `-2.504` n `238`; crypto_major avg `-1.5306` n `8`; equity avg `-1.5104` n `154`; fx avg `0.0535` n `6`; index avg `-0.0489` n `27`; metal avg `-0.2903` n `20`; unknown avg `30.2298` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
