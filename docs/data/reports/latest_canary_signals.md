# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T19:37:45.135105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.1309` n `230`; crypto_major avg `-0.12` n `8`; equity avg `-0.2395` n `102`; fx avg `-0.002` n `6`; index avg `-0.0554` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.5752` n `780`
- 1h: commodity avg `0.0713` n `12`; crypto_alt avg `-0.1665` n `230`; crypto_major avg `-0.0998` n `8`; equity avg `-0.1954` n `102`; fx avg `0.0247` n `6`; index avg `-0.029` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.1273` n `780`
- 4h: commodity avg `0.0727` n `12`; crypto_alt avg `0.0202` n `230`; crypto_major avg `-0.2075` n `8`; equity avg `0.5513` n `102`; fx avg `0.0922` n `6`; index avg `0.127` n `25`; metal avg `0.1015` n `20`; unknown avg `5.6213` n `780`
- 24h: commodity avg `0.2898` n `12`; crypto_alt avg `-0.5934` n `230`; crypto_major avg `-2.2276` n `8`; equity avg `0.134` n `102`; fx avg `0.2239` n `6`; index avg `0.2207` n `25`; metal avg `-0.3723` n `20`; unknown avg `0.2898` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
