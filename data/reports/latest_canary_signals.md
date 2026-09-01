# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T16:52:31.511594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0617` n `12`; crypto_alt avg `0.0448` n `232`; crypto_major avg `0.1323` n `8`; equity avg `0.1019` n `131`; fx avg `-0.0022` n `6`; index avg `0.0122` n `26`; metal avg `0.0444` n `20`; unknown avg `0.0444` n `793`
- 1h: commodity avg `0.2509` n `12`; crypto_alt avg `-0.8735` n `232`; crypto_major avg `-0.7609` n `8`; equity avg `-0.5801` n `131`; fx avg `0.0025` n `6`; index avg `-0.146` n `26`; metal avg `-0.1073` n `20`; unknown avg `0.2161` n `791`
- 4h: commodity avg `0.359` n `12`; crypto_alt avg `-0.2699` n `232`; crypto_major avg `-0.6255` n `8`; equity avg `-0.3135` n `131`; fx avg `-0.0252` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0631` n `20`; unknown avg `-0.0412` n `790`
- 24h: commodity avg `0.6521` n `12`; crypto_alt avg `0.201` n `232`; crypto_major avg `-1.1286` n `8`; equity avg `-1.4392` n `130`; fx avg `0.0363` n `6`; index avg `-0.2236` n `26`; metal avg `-0.5623` n `20`; unknown avg `-0.1842` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0366`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0334`, n `668`, weak_sample_signal
