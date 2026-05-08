# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T20:37:16.018952+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `12`; crypto_alt avg `0.0656` n `228`; crypto_major avg `0.0338` n `8`; equity avg `-0.0625` n `65`; fx avg `-0.0032` n `5`; index avg `0.0044` n `23`; metal avg `0.0485` n `18`; unknown avg `0.0067` n `375`
- 1h: commodity avg `-0.1721` n `12`; crypto_alt avg `-0.0111` n `228`; crypto_major avg `0.0011` n `8`; equity avg `0.336` n `65`; fx avg `-0.0094` n `5`; index avg `0.0619` n `23`; metal avg `-0.1734` n `18`; unknown avg `-0.2622` n `375`
- 4h: commodity avg `-0.6608` n `12`; crypto_alt avg `1.1196` n `228`; crypto_major avg `1.2227` n `8`; equity avg `1.1689` n `65`; fx avg `0.0555` n `5`; index avg `0.3268` n `23`; metal avg `0.1585` n `18`; unknown avg `-0.0584` n `375`
- 24h: commodity avg `-0.591` n `12`; crypto_alt avg `3.1925` n `228`; crypto_major avg `1.5435` n `8`; equity avg `3.4935` n `65`; fx avg `0.2113` n `5`; index avg `1.4966` n `23`; metal avg `0.7623` n `18`; unknown avg `0.6605` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
