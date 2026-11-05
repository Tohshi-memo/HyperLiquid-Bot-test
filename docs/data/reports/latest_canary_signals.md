# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T13:07:25.250403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0808` n `13`; crypto_alt avg `0.0929` n `239`; crypto_major avg `0.0991` n `8`; equity avg `-0.1054` n `158`; fx avg `0.0015` n `6`; index avg `-0.0078` n `27`; metal avg `0.017` n `20`; unknown avg `0.5496` n `1249`
- 1h: commodity avg `0.1084` n `13`; crypto_alt avg `-0.5083` n `239`; crypto_major avg `-0.6107` n `8`; equity avg `-0.8282` n `158`; fx avg `0.0112` n `6`; index avg `-0.0708` n `27`; metal avg `-0.0039` n `20`; unknown avg `0.756` n `1253`
- 4h: commodity avg `0.4366` n `13`; crypto_alt avg `-1.3559` n `239`; crypto_major avg `-1.0044` n `8`; equity avg `-0.9094` n `158`; fx avg `0.0077` n `6`; index avg `-0.0466` n `27`; metal avg `0.0623` n `20`; unknown avg `172.7974` n `1201`
- 24h: commodity avg `-0.9424` n `13`; crypto_alt avg `0.079` n `239`; crypto_major avg `1.1906` n `8`; equity avg `-2.4615` n `158`; fx avg `-0.0152` n `6`; index avg `-0.2518` n `27`; metal avg `0.7332` n `20`; unknown avg `194.077` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
