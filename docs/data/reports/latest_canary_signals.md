# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T04:07:28.888271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `-0.1321` n `230`; crypto_major avg `-0.0568` n `8`; equity avg `-0.15` n `120`; fx avg `-0.0009` n `6`; index avg `-0.0374` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.933` n `789`
- 1h: commodity avg `-0.0357` n `12`; crypto_alt avg `0.2237` n `230`; crypto_major avg `0.1367` n `8`; equity avg `-0.2304` n `120`; fx avg `0.0065` n `6`; index avg `-0.041` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.1401` n `789`
- 4h: commodity avg `0.0434` n `12`; crypto_alt avg `0.137` n `230`; crypto_major avg `-0.1215` n `8`; equity avg `0.446` n `120`; fx avg `-0.146` n `6`; index avg `-0.0098` n `25`; metal avg `0.077` n `20`; unknown avg `0.4698` n `789`
- 24h: commodity avg `0.2844` n `12`; crypto_alt avg `0.6766` n `230`; crypto_major avg `0.325` n `8`; equity avg `-3.2139` n `120`; fx avg `-0.1434` n `6`; index avg `-0.535` n `25`; metal avg `-0.5161` n `20`; unknown avg `-0.1231` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
