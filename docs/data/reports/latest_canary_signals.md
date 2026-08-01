# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T13:52:23.108150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `-0.0588` n `8`; equity avg `-0.0079` n `102`; fx avg `0.0053` n `6`; index avg `-0.0029` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0302` n `782`
- 1h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.0466` n `230`; crypto_major avg `-0.0067` n `8`; equity avg `-0.0524` n `102`; fx avg `0.0088` n `6`; index avg `0.0041` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0557` n `782`
- 4h: commodity avg `0.0989` n `12`; crypto_alt avg `0.0332` n `230`; crypto_major avg `-0.008` n `8`; equity avg `-0.0725` n `102`; fx avg `-0.052` n `6`; index avg `-0.0474` n `25`; metal avg `-0.0041` n `20`; unknown avg `-0.1306` n `781`
- 24h: commodity avg `0.4413` n `12`; crypto_alt avg `0.6301` n `230`; crypto_major avg `-0.6729` n `8`; equity avg `-1.011` n `102`; fx avg `0.0123` n `6`; index avg `-0.0323` n `25`; metal avg `0.2631` n `20`; unknown avg `4.4306` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
