# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T03:22:25.356738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.0053` n `230`; crypto_major avg `0.0562` n `8`; equity avg `0.0101` n `113`; fx avg `0.0022` n `6`; index avg `0.0153` n `25`; metal avg `0.034` n `20`; unknown avg `-0.0437` n `785`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `0.0946` n `8`; equity avg `0.1257` n `113`; fx avg `-0.0171` n `6`; index avg `0.0469` n `25`; metal avg `-0.0826` n `20`; unknown avg `0.0552` n `785`
- 4h: commodity avg `0.0465` n `12`; crypto_alt avg `0.2515` n `230`; crypto_major avg `0.2741` n `8`; equity avg `0.6061` n `113`; fx avg `-0.0461` n `6`; index avg `0.1577` n `25`; metal avg `0.1211` n `20`; unknown avg `-0.2073` n `785`
- 24h: commodity avg `0.849` n `12`; crypto_alt avg `-0.5679` n `230`; crypto_major avg `-0.5399` n `8`; equity avg `-0.9729` n `113`; fx avg `0.1149` n `6`; index avg `0.0401` n `25`; metal avg `0.5645` n `20`; unknown avg `103.8177` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1614`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
