# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T22:05:56.532863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `0.3367` n `230`; crypto_major avg `0.3271` n `8`; equity avg `0.0255` n `121`; fx avg `0.0066` n `6`; index avg `0.0092` n `25`; metal avg `-0.0154` n `20`; unknown avg `0.2478` n `794`
- 1h: commodity avg `0.0208` n `12`; crypto_alt avg `-0.8135` n `230`; crypto_major avg `-0.6041` n `8`; equity avg `0.0252` n `121`; fx avg `0.0064` n `6`; index avg `0.0095` n `25`; metal avg `-0.0008` n `20`; unknown avg `0.0484` n `794`
- 4h: commodity avg `0.0834` n `12`; crypto_alt avg `-1.7221` n `230`; crypto_major avg `-0.6097` n `8`; equity avg `0.0934` n `121`; fx avg `0.0341` n `6`; index avg `0.001` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.5461` n `794`
- 24h: commodity avg `0.0585` n `12`; crypto_alt avg `-2.7101` n `230`; crypto_major avg `-0.5551` n `8`; equity avg `-0.4067` n `121`; fx avg `0.0771` n `6`; index avg `-0.0515` n `25`; metal avg `-0.079` n `20`; unknown avg `1.905` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
