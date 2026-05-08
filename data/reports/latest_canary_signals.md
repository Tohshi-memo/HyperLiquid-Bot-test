# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T21:52:19.787689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0837` n `12`; crypto_alt avg `0.103` n `228`; crypto_major avg `0.0167` n `8`; equity avg `-0.0354` n `65`; fx avg `-0.0025` n `5`; index avg `0.0376` n `23`; metal avg `-0.0144` n `18`; unknown avg `-0.1301` n `375`
- 1h: commodity avg `-0.0303` n `12`; crypto_alt avg `0.5332` n `228`; crypto_major avg `0.2158` n `8`; equity avg `0.0871` n `65`; fx avg `-0.0298` n `5`; index avg `0.0626` n `23`; metal avg `0.0075` n `18`; unknown avg `-0.2689` n `375`
- 4h: commodity avg `-0.4563` n `12`; crypto_alt avg `0.8047` n `228`; crypto_major avg `0.4058` n `8`; equity avg `1.0652` n `65`; fx avg `0.0131` n `5`; index avg `0.1086` n `23`; metal avg `-0.029` n `18`; unknown avg `-0.226` n `375`
- 24h: commodity avg `-0.8898` n `12`; crypto_alt avg `3.7058` n `228`; crypto_major avg `1.5989` n `8`; equity avg `4.586` n `65`; fx avg `0.2195` n `5`; index avg `1.7819` n `23`; metal avg `1.2143` n `18`; unknown avg `0.7956` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
