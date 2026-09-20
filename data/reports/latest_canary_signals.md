# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T21:29:40.610938+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `12`; crypto_alt avg `0.0712` n `234`; crypto_major avg `-0.0673` n `8`; equity avg `-0.0302` n `140`; fx avg `-0.0397` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0228` n `20`; unknown avg `32.4761` n `925`
- 1h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.308` n `234`; crypto_major avg `-0.3726` n `8`; equity avg `0.0028` n `140`; fx avg `-0.0192` n `6`; index avg `0.0249` n `26`; metal avg `-0.023` n `20`; unknown avg `0.1561` n `887`
- 4h: commodity avg `0.0082` n `12`; crypto_alt avg `0.1045` n `234`; crypto_major avg `-0.2084` n `8`; equity avg `-0.0016` n `140`; fx avg `-0.0499` n `6`; index avg `0.0135` n `26`; metal avg `-0.049` n `20`; unknown avg `1.5908` n `873`
- 24h: commodity avg `0.3361` n `12`; crypto_alt avg `1.0692` n `234`; crypto_major avg `-0.2258` n `8`; equity avg `-0.0991` n `140`; fx avg `-0.0269` n `6`; index avg `-0.0325` n `26`; metal avg `-0.0681` n `20`; unknown avg `3.3046` n `777`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
