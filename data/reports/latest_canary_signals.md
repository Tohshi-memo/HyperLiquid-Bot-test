# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T13:01:24.815546+00:00`
- Correlation status: `ready`
- Asset price records: `648`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.0406` n `228`; crypto_major avg `-0.0073` n `8`; equity avg `0.0102` n `65`; fx avg `-0.0045` n `5`; index avg `-0.0295` n `23`; metal avg `-0.1599` n `18`; unknown avg `-0.0196` n `375`
- 1h: commodity avg `0.183` n `12`; crypto_alt avg `-0.1415` n `228`; crypto_major avg `-0.2496` n `8`; equity avg `0.2525` n `65`; fx avg `-0.0238` n `5`; index avg `0.1508` n `23`; metal avg `0.1408` n `18`; unknown avg `-0.2662` n `375`
- 4h: commodity avg `0.2047` n `12`; crypto_alt avg `0.203` n `228`; crypto_major avg `-0.0157` n `8`; equity avg `0.1295` n `65`; fx avg `-0.0255` n `5`; index avg `0.1891` n `23`; metal avg `0.1366` n `18`; unknown avg `-0.0075` n `375`
- 24h: commodity avg `1.8834` n `12`; crypto_alt avg `0.4145` n `228`; crypto_major avg `-1.5472` n `8`; equity avg `-0.2189` n `65`; fx avg `0.2147` n `5`; index avg `-0.0641` n `23`; metal avg `-0.6673` n `18`; unknown avg `-0.6691` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1296`, n `640`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1279`, n `640`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `644`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0952`, n `644`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `644`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0908`, n `640`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `640`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.088`, n `644`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `644`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `644`, weak_sample_signal
