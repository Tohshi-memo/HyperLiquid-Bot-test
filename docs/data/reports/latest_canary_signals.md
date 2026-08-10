# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T23:07:27.623432+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `12`; crypto_alt avg `-0.0328` n `230`; crypto_major avg `0.0045` n `8`; equity avg `-0.1024` n `113`; fx avg `0.0041` n `6`; index avg `-0.008` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0717` n `785`
- 1h: commodity avg `-0.0463` n `12`; crypto_alt avg `0.0905` n `230`; crypto_major avg `0.0689` n `8`; equity avg `-0.1868` n `113`; fx avg `0.0034` n `6`; index avg `-0.0284` n `25`; metal avg `0.0406` n `20`; unknown avg `-0.0907` n `785`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.3241` n `230`; crypto_major avg `0.0031` n `8`; equity avg `-0.5818` n `113`; fx avg `0.0178` n `6`; index avg `-0.0527` n `25`; metal avg `0.0658` n `20`; unknown avg `2.8449` n `785`
- 24h: commodity avg `0.8317` n `12`; crypto_alt avg `-0.8921` n `230`; crypto_major avg `-0.8003` n `8`; equity avg `-1.8349` n `113`; fx avg `0.2569` n `6`; index avg `-0.0874` n `25`; metal avg `0.3564` n `20`; unknown avg `103.6096` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
