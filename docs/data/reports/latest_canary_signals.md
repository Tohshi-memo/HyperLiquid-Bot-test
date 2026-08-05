# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T03:52:28.110019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `-0.0124` n `8`; equity avg `0.0833` n `108`; fx avg `-0.0057` n `6`; index avg `0.0249` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.0312` n `781`
- 1h: commodity avg `0.0211` n `12`; crypto_alt avg `-0.2386` n `230`; crypto_major avg `-0.5131` n `8`; equity avg `0.3099` n `108`; fx avg `-0.0014` n `6`; index avg `0.0435` n `25`; metal avg `-0.0312` n `20`; unknown avg `0.4781` n `781`
- 4h: commodity avg `-0.0595` n `12`; crypto_alt avg `0.2994` n `230`; crypto_major avg `0.1259` n `8`; equity avg `0.6294` n `108`; fx avg `-0.0883` n `6`; index avg `0.0748` n `25`; metal avg `0.3788` n `20`; unknown avg `-0.2074` n `781`
- 24h: commodity avg `-1.5054` n `12`; crypto_alt avg `0.096` n `230`; crypto_major avg `0.3572` n `8`; equity avg `4.0352` n `108`; fx avg `-0.0115` n `6`; index avg `0.8591` n `25`; metal avg `1.0508` n `20`; unknown avg `0.3665` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
