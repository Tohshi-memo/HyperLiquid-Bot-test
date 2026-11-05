# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T05:07:33.658294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `-0.3599` n `239`; crypto_major avg `-0.1856` n `8`; equity avg `-0.2206` n `158`; fx avg `-0.0012` n `6`; index avg `-0.0217` n `27`; metal avg `-0.048` n `20`; unknown avg `3.2865` n `1257`
- 1h: commodity avg `-0.0213` n `13`; crypto_alt avg `-0.3506` n `239`; crypto_major avg `-0.0042` n `8`; equity avg `-0.3505` n `158`; fx avg `-0.024` n `6`; index avg `-0.0602` n `27`; metal avg `-0.0917` n `20`; unknown avg `3.3689` n `1251`
- 4h: commodity avg `-0.2598` n `13`; crypto_alt avg `0.0278` n `239`; crypto_major avg `-0.148` n `8`; equity avg `-0.5227` n `158`; fx avg `0.062` n `6`; index avg `-0.1455` n `27`; metal avg `0.2599` n `20`; unknown avg `0.7926` n `1236`
- 24h: commodity avg `-2.0774` n `13`; crypto_alt avg `2.3003` n `239`; crypto_major avg `2.9089` n `8`; equity avg `-0.8139` n `158`; fx avg `0.0996` n `6`; index avg `0.1017` n `27`; metal avg `1.6901` n `20`; unknown avg `32.6416` n `1018`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2545`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
