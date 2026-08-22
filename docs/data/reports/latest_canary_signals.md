# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T02:07:30.160604+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.4331` n `230`; crypto_major avg `0.5` n `8`; equity avg `0.0325` n `121`; fx avg `-0.0035` n `6`; index avg `0.0026` n `25`; metal avg `-0.0119` n `20`; unknown avg `-0.0258` n `793`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.1587` n `230`; crypto_major avg `0.3394` n `8`; equity avg `0.0188` n `121`; fx avg `0.0057` n `6`; index avg `0.001` n `25`; metal avg `-0.0245` n `20`; unknown avg `-0.0243` n `793`
- 4h: commodity avg `-0.0288` n `12`; crypto_alt avg `1.1301` n `230`; crypto_major avg `0.1545` n `8`; equity avg `0.0028` n `121`; fx avg `0.0062` n `6`; index avg `0.0118` n `25`; metal avg `-0.0356` n `20`; unknown avg `0.179` n `793`
- 24h: commodity avg `0.0255` n `12`; crypto_alt avg `9.001` n `230`; crypto_major avg `6.7355` n `8`; equity avg `0.2069` n `121`; fx avg `0.0516` n `6`; index avg `0.0172` n `25`; metal avg `0.2944` n `20`; unknown avg `1.2613` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
