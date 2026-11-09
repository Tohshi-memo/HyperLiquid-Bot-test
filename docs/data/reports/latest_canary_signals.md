# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T20:07:32.551947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1352` n `13`; crypto_alt avg `-0.1919` n `239`; crypto_major avg `-0.1318` n `8`; equity avg `0.1669` n `160`; fx avg `0.0047` n `6`; index avg `0.0185` n `27`; metal avg `0.0494` n `20`; unknown avg `1.2599` n `1249`
- 1h: commodity avg `-0.3714` n `13`; crypto_alt avg `-0.1317` n `239`; crypto_major avg `0.0439` n `8`; equity avg `0.4099` n `160`; fx avg `-0.0366` n `6`; index avg `0.0572` n `27`; metal avg `0.2439` n `20`; unknown avg `1.0255` n `1245`
- 4h: commodity avg `-0.4024` n `13`; crypto_alt avg `-0.7793` n `239`; crypto_major avg `-0.6878` n `8`; equity avg `-0.0931` n `160`; fx avg `-0.0208` n `6`; index avg `0.0738` n `27`; metal avg `0.1241` n `20`; unknown avg `0.1591` n `1245`
- 24h: commodity avg `-0.4818` n `13`; crypto_alt avg `0.592` n `239`; crypto_major avg `-2.4258` n `8`; equity avg `3.9945` n `160`; fx avg `-0.1615` n `6`; index avg `0.4952` n `27`; metal avg `0.6462` n `20`; unknown avg `6.1968` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
