# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T21:37:20.600562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `0.2469` n `228`; crypto_major avg `0.1198` n `8`; equity avg `0.1454` n `65`; fx avg `-0.0085` n `5`; index avg `0.0457` n `23`; metal avg `-0.0152` n `18`; unknown avg `0.1893` n `375`
- 1h: commodity avg `0.0903` n `12`; crypto_alt avg `0.3307` n `228`; crypto_major avg `0.0817` n `8`; equity avg `0.1183` n `65`; fx avg `-0.0241` n `5`; index avg `-0.0233` n `23`; metal avg `-0.0013` n `18`; unknown avg `0.0468` n `375`
- 4h: commodity avg `-0.3355` n `12`; crypto_alt avg `0.7393` n `228`; crypto_major avg `0.4925` n `8`; equity avg `0.9697` n `65`; fx avg `0.0158` n `5`; index avg `0.001` n `23`; metal avg `-0.0423` n `18`; unknown avg `-0.302` n `375`
- 24h: commodity avg `-0.9973` n `12`; crypto_alt avg `3.6051` n `228`; crypto_major avg `1.5612` n `8`; equity avg `4.2948` n `65`; fx avg `0.2067` n `5`; index avg `1.6773` n `23`; metal avg `1.2443` n `18`; unknown avg `1.0696` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
