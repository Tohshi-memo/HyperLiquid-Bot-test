# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T03:52:26.708709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0149` n `13`; crypto_alt avg `-0.1811` n `239`; crypto_major avg `-0.2922` n `8`; equity avg `-0.1949` n `158`; fx avg `0.0017` n `6`; index avg `-0.0539` n `27`; metal avg `-0.0222` n `20`; unknown avg `0.1188` n `1265`
- 1h: commodity avg `-0.101` n `13`; crypto_alt avg `0.1144` n `239`; crypto_major avg `-0.078` n `8`; equity avg `-0.3037` n `158`; fx avg `0.0219` n `6`; index avg `-0.0666` n `27`; metal avg `-0.0266` n `20`; unknown avg `7.7623` n `1257`
- 4h: commodity avg `-0.3803` n `13`; crypto_alt avg `0.491` n `239`; crypto_major avg `0.0163` n `8`; equity avg `-0.8278` n `158`; fx avg `0.0441` n `6`; index avg `-0.2178` n `27`; metal avg `0.4314` n `20`; unknown avg `0.7022` n `1248`
- 24h: commodity avg `-1.8331` n `13`; crypto_alt avg `4.5988` n `239`; crypto_major avg `4.413` n `8`; equity avg `1.0777` n `158`; fx avg `0.145` n `6`; index avg `0.4312` n `27`; metal avg `1.9732` n `20`; unknown avg `33.883` n `1032`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2513`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1976`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1949`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
