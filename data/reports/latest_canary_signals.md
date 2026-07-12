# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T10:42:49.769400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.0687` n `230`; crypto_major avg `-0.0917` n `8`; equity avg `-0.0507` n `92`; fx avg `0.0015` n `6`; index avg `-0.0098` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.1179` n `765`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0055` n `92`; fx avg `0.0053` n `6`; index avg `0.003` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.1871` n `765`
- 4h: commodity avg `0.0964` n `12`; crypto_alt avg `0.1162` n `230`; crypto_major avg `0.2378` n `8`; equity avg `0.0187` n `92`; fx avg `0.0085` n `6`; index avg `0.0192` n `25`; metal avg `-0.0113` n `20`; unknown avg `1.676` n `763`
- 24h: commodity avg `0.4823` n `12`; crypto_alt avg `-0.8644` n `230`; crypto_major avg `-0.7149` n `8`; equity avg `-0.2017` n `92`; fx avg `0.0096` n `6`; index avg `-0.1242` n `25`; metal avg `-0.1151` n `20`; unknown avg `0.0257` n `747`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
