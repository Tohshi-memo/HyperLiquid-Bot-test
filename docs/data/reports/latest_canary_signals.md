# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T20:22:30.791992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0424` n `13`; crypto_alt avg `0.3088` n `239`; crypto_major avg `0.2557` n `8`; equity avg `0.356` n `160`; fx avg `0.0071` n `6`; index avg `0.0435` n `27`; metal avg `0.0446` n `20`; unknown avg `0.0304` n `1261`
- 1h: commodity avg `-0.358` n `13`; crypto_alt avg `0.2556` n `239`; crypto_major avg `0.3313` n `8`; equity avg `0.8107` n `160`; fx avg `-0.0233` n `6`; index avg `0.1075` n `27`; metal avg `0.2942` n `20`; unknown avg `2.4004` n `1245`
- 4h: commodity avg `-0.3023` n `13`; crypto_alt avg `-0.0392` n `239`; crypto_major avg `-0.1216` n `8`; equity avg `0.7092` n `160`; fx avg `-0.0224` n `6`; index avg `0.1508` n `27`; metal avg `0.2532` n `20`; unknown avg `0.6562` n `1245`
- 24h: commodity avg `-0.4555` n `13`; crypto_alt avg `0.8941` n `239`; crypto_major avg `-2.212` n `8`; equity avg `4.4179` n `160`; fx avg `-0.1568` n `6`; index avg `0.5441` n `27`; metal avg `0.6991` n `20`; unknown avg `7.2356` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
