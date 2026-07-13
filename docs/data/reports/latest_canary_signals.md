# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T23:07:23.422176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0329` n `12`; crypto_alt avg `-0.1555` n `230`; crypto_major avg `-0.1123` n `8`; equity avg `-0.3485` n `92`; fx avg `-0.0069` n `6`; index avg `-0.0384` n `25`; metal avg `-0.021` n `20`; unknown avg `0.1712` n `766`
- 1h: commodity avg `0.1562` n `12`; crypto_alt avg `-0.1301` n `230`; crypto_major avg `-0.2072` n `8`; equity avg `-0.4379` n `92`; fx avg `-0.0268` n `6`; index avg `-0.0775` n `25`; metal avg `-0.0186` n `20`; unknown avg `-0.0417` n `766`
- 4h: commodity avg `0.2369` n `12`; crypto_alt avg `-0.5407` n `230`; crypto_major avg `-0.273` n `8`; equity avg `-0.3892` n `92`; fx avg `-0.0309` n `6`; index avg `-0.1359` n `25`; metal avg `0.0075` n `20`; unknown avg `-0.3431` n `766`
- 24h: commodity avg `1.0238` n `12`; crypto_alt avg `-2.1385` n `230`; crypto_major avg `-2.64` n `8`; equity avg `-3.344` n `92`; fx avg `-0.0547` n `6`; index avg `-0.6429` n `25`; metal avg `-0.2859` n `20`; unknown avg `-0.3982` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
