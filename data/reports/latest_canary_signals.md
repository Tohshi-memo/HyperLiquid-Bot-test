# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T21:52:31.149065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.1901` n `234`; crypto_major avg `0.0404` n `8`; equity avg `0.0274` n `141`; fx avg `-0.0013` n `6`; index avg `0.0021` n `26`; metal avg `0.0245` n `20`; unknown avg `-0.131` n `945`
- 1h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.3453` n `234`; crypto_major avg `0.4288` n `8`; equity avg `0.0476` n `141`; fx avg `-0.0047` n `6`; index avg `-0.004` n `26`; metal avg `0.0216` n `20`; unknown avg `-0.0862` n `927`
- 4h: commodity avg `0.22` n `12`; crypto_alt avg `-0.8885` n `234`; crypto_major avg `-0.0662` n `8`; equity avg `-0.2468` n `141`; fx avg `-0.019` n `6`; index avg `-0.016` n `26`; metal avg `0.0406` n `20`; unknown avg `3.3624` n `845`
- 24h: commodity avg `0.5833` n `12`; crypto_alt avg `-3.8145` n `234`; crypto_major avg `-3.3809` n `8`; equity avg `-1.5611` n `140`; fx avg `0.0071` n `6`; index avg `-0.355` n `26`; metal avg `-0.7717` n `20`; unknown avg `584.7645` n `820`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
