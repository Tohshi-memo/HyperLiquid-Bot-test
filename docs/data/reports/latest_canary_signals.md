# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T01:03:14.123236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0833` n `12`; crypto_alt avg `0.0905` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.1391` n `108`; fx avg `0.0122` n `6`; index avg `-0.0355` n `25`; metal avg `0.1225` n `20`; unknown avg `0.3272` n `782`
- 1h: commodity avg `0.0509` n `12`; crypto_alt avg `0.1657` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.621` n `108`; fx avg `-0.0619` n `6`; index avg `-0.1724` n `25`; metal avg `0.2213` n `20`; unknown avg `-0.0613` n `782`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `-0.2174` n `8`; equity avg `-0.656` n `108`; fx avg `-0.0461` n `6`; index avg `-0.1854` n `25`; metal avg `0.3445` n `20`; unknown avg `0.0156` n `782`
- 24h: commodity avg `-0.1816` n `12`; crypto_alt avg `0.9982` n `230`; crypto_major avg `0.8854` n `8`; equity avg `-1.6542` n `108`; fx avg `-0.0234` n `6`; index avg `-0.3354` n `25`; metal avg `1.1898` n `20`; unknown avg `1.0949` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
