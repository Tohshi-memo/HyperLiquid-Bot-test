# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T09:37:26.435279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1395` n `12`; crypto_alt avg `0.2999` n `228`; crypto_major avg `0.0606` n `8`; equity avg `-0.0284` n `74`; fx avg `-0.0213` n `6`; index avg `-0.0232` n `23`; metal avg `-0.1269` n `18`; unknown avg `-0.1967` n `424`
- 1h: commodity avg `0.2474` n `12`; crypto_alt avg `0.9776` n `228`; crypto_major avg `0.6217` n `8`; equity avg `0.1092` n `74`; fx avg `-0.002` n `6`; index avg `0.0717` n `23`; metal avg `0.0903` n `18`; unknown avg `-0.06` n `424`
- 4h: commodity avg `-0.3334` n `12`; crypto_alt avg `-2.0217` n `228`; crypto_major avg `-0.9044` n `8`; equity avg `-0.1483` n `74`; fx avg `0.055` n `6`; index avg `0.0365` n `23`; metal avg `0.2141` n `18`; unknown avg `-0.1892` n `404`
- 24h: commodity avg `-0.2831` n `12`; crypto_alt avg `-3.2725` n `228`; crypto_major avg `-2.2339` n `8`; equity avg `-0.4326` n `73`; fx avg `0.0846` n `6`; index avg `-0.0415` n `23`; metal avg `-0.5484` n `18`; unknown avg `-0.2995` n `402`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
