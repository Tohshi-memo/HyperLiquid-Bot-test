# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T06:22:29.382040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0613` n `12`; crypto_alt avg `-0.0217` n `230`; crypto_major avg `0.0004` n `8`; equity avg `-0.0595` n `113`; fx avg `0.0031` n `6`; index avg `-0.0149` n `25`; metal avg `-0.0738` n `20`; unknown avg `0.0406` n `785`
- 1h: commodity avg `0.0617` n `12`; crypto_alt avg `-0.0083` n `230`; crypto_major avg `0.0755` n `8`; equity avg `-0.1528` n `113`; fx avg `0.0199` n `6`; index avg `-0.0279` n `25`; metal avg `-0.1567` n `20`; unknown avg `0.0147` n `753`
- 4h: commodity avg `0.101` n `12`; crypto_alt avg `-0.3927` n `230`; crypto_major avg `-0.0909` n `8`; equity avg `-0.0023` n `113`; fx avg `-0.0062` n `6`; index avg `0.0137` n `25`; metal avg `-0.3858` n `20`; unknown avg `0.0099` n `753`
- 24h: commodity avg `1.0554` n `12`; crypto_alt avg `-0.9874` n `230`; crypto_major avg `-0.8277` n `8`; equity avg `-1.2202` n `113`; fx avg `0.0688` n `6`; index avg `-0.0099` n `25`; metal avg `0.1125` n `20`; unknown avg `0.186` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
