# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T23:37:24.920866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0714` n `12`; crypto_alt avg `0.4131` n `228`; crypto_major avg `0.6145` n `8`; equity avg `0.021` n `74`; fx avg `-0.0035` n `6`; index avg `-0.0127` n `23`; metal avg `-0.1227` n `18`; unknown avg `-0.0198` n `424`
- 1h: commodity avg `0.0193` n `12`; crypto_alt avg `0.7044` n `228`; crypto_major avg `0.7472` n `8`; equity avg `-0.1591` n `74`; fx avg `0.001` n `6`; index avg `-0.1458` n `23`; metal avg `-0.2266` n `18`; unknown avg `0.0384` n `424`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `-2.2175` n `228`; crypto_major avg `-0.952` n `8`; equity avg `-1.2109` n `74`; fx avg `0.0067` n `6`; index avg `-0.4737` n `23`; metal avg `-0.3516` n `18`; unknown avg `-1.0507` n `424`
- 24h: commodity avg `-0.5005` n `12`; crypto_alt avg `-6.4722` n `228`; crypto_major avg `-3.9153` n `8`; equity avg `-0.1772` n `73`; fx avg `0.0562` n `6`; index avg `0.1381` n `23`; metal avg `0.4382` n `18`; unknown avg `-1.4884` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
