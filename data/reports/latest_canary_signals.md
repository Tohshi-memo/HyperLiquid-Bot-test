# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T21:07:19.044485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0972` n `12`; crypto_alt avg `0.2069` n `228`; crypto_major avg `-0.0147` n `8`; equity avg `-0.0731` n `65`; fx avg `-0.0003` n `5`; index avg `-0.0314` n `23`; metal avg `0.041` n `18`; unknown avg `0.4086` n `375`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `0.2626` n `228`; crypto_major avg `-0.0488` n `8`; equity avg `0.0228` n `65`; fx avg `0.0075` n `5`; index avg `-0.1228` n `23`; metal avg `-0.0817` n `18`; unknown avg `0.4728` n `375`
- 4h: commodity avg `-0.3687` n `12`; crypto_alt avg `1.047` n `228`; crypto_major avg `0.9315` n `8`; equity avg `1.1197` n `65`; fx avg `0.0451` n `5`; index avg `0.1514` n `23`; metal avg `0.1336` n `18`; unknown avg `0.1181` n `375`
- 24h: commodity avg `-0.984` n `12`; crypto_alt avg `3.8495` n `228`; crypto_major avg `1.5527` n `8`; equity avg `3.7277` n `65`; fx avg `0.2477` n `5`; index avg `1.4552` n `23`; metal avg `1.2182` n `18`; unknown avg `1.0032` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
