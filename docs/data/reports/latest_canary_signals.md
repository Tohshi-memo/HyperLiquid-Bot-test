# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T04:52:29.558347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `-0.0347` n `230`; crypto_major avg `-0.0707` n `8`; equity avg `-0.0008` n `113`; fx avg `0.0125` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0435` n `20`; unknown avg `0.5494` n `785`
- 1h: commodity avg `0.0009` n `12`; crypto_alt avg `-0.1275` n `230`; crypto_major avg `-0.0311` n `8`; equity avg `0.0678` n `113`; fx avg `-0.0044` n `6`; index avg `0.0232` n `25`; metal avg `-0.0754` n `20`; unknown avg `-0.0764` n `785`
- 4h: commodity avg `-0.0343` n `12`; crypto_alt avg `-0.1329` n `230`; crypto_major avg `0.2604` n `8`; equity avg `0.4251` n `113`; fx avg `0.005` n `6`; index avg `0.1407` n `25`; metal avg `-0.0615` n `20`; unknown avg `-0.1256` n `785`
- 24h: commodity avg `0.887` n `12`; crypto_alt avg `-0.5067` n `230`; crypto_major avg `-0.4` n `8`; equity avg `-0.7398` n `113`; fx avg `0.0999` n `6`; index avg `0.1017` n `25`; metal avg `0.437` n `20`; unknown avg `103.8799` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
