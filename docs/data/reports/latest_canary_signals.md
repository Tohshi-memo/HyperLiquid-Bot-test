# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T10:37:29.474424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `0.0634` n `239`; crypto_major avg `0.1016` n `8`; equity avg `0.1356` n `158`; fx avg `-0.0023` n `6`; index avg `0.0036` n `27`; metal avg `-0.0412` n `20`; unknown avg `-0.1213` n `1264`
- 1h: commodity avg `-0.2723` n `13`; crypto_alt avg `0.1602` n `239`; crypto_major avg `0.2672` n `8`; equity avg `0.7371` n `158`; fx avg `-0.0334` n `6`; index avg `0.0566` n `27`; metal avg `0.0795` n `20`; unknown avg `0.5335` n `1258`
- 4h: commodity avg `-0.3047` n `13`; crypto_alt avg `0.6137` n `239`; crypto_major avg `0.9164` n `8`; equity avg `1.4044` n `158`; fx avg `0.0532` n `6`; index avg `0.2548` n `27`; metal avg `0.3026` n `20`; unknown avg `11.0842` n `1166`
- 24h: commodity avg `-0.6477` n `13`; crypto_alt avg `2.4557` n `239`; crypto_major avg `1.6736` n `8`; equity avg `2.8793` n `158`; fx avg `0.1415` n `6`; index avg `0.2533` n `27`; metal avg `1.1914` n `20`; unknown avg `1.0687` n `1057`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.264`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
