# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T01:22:23.099894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1955` n `12`; crypto_alt avg `-0.1016` n `228`; crypto_major avg `-0.0159` n `8`; equity avg `-0.0995` n `74`; fx avg `0.0363` n `6`; index avg `-0.0756` n `23`; metal avg `-0.3077` n `18`; unknown avg `-0.0332` n `424`
- 1h: commodity avg `-0.0713` n `12`; crypto_alt avg `-0.7047` n `228`; crypto_major avg `-0.4128` n `8`; equity avg `-0.3986` n `74`; fx avg `0.0817` n `6`; index avg `-0.2088` n `23`; metal avg `-0.4148` n `18`; unknown avg `0.0442` n `424`
- 4h: commodity avg `-0.1647` n `12`; crypto_alt avg `-1.5145` n `228`; crypto_major avg `-0.8169` n `8`; equity avg `-1.6482` n `74`; fx avg `0.1236` n `6`; index avg `-0.8331` n `23`; metal avg `-0.9157` n `18`; unknown avg `0.121` n `424`
- 24h: commodity avg `-0.3416` n `12`; crypto_alt avg `-4.6691` n `228`; crypto_major avg `-2.4633` n `8`; equity avg `-1.6696` n `73`; fx avg `0.2077` n `6`; index avg `-0.6425` n `23`; metal avg `-0.7555` n `18`; unknown avg `-0.1243` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
