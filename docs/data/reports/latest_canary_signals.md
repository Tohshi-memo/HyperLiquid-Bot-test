# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T10:07:33.484148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1485` n `13`; crypto_alt avg `0.1859` n `239`; crypto_major avg `-0.0145` n `8`; equity avg `-0.1941` n `158`; fx avg `0.0014` n `6`; index avg `-0.0357` n `27`; metal avg `-0.0171` n `20`; unknown avg `-0.0137` n `1250`
- 1h: commodity avg `-0.0812` n `13`; crypto_alt avg `0.2503` n `239`; crypto_major avg `0.0565` n `8`; equity avg `0.0827` n `158`; fx avg `-0.0221` n `6`; index avg `0.0251` n `27`; metal avg `-0.1213` n `20`; unknown avg `-0.1895` n `1252`
- 4h: commodity avg `-0.3479` n `13`; crypto_alt avg `1.2095` n `239`; crypto_major avg `0.6654` n `8`; equity avg `1.7007` n `158`; fx avg `-0.1233` n `6`; index avg `0.2166` n `27`; metal avg `0.2054` n `20`; unknown avg `227.5656` n `1184`
- 24h: commodity avg `0.5988` n `13`; crypto_alt avg `-3.6279` n `239`; crypto_major avg `-5.5729` n `8`; equity avg `-4.9379` n `158`; fx avg `-0.0409` n `6`; index avg `-0.636` n `27`; metal avg `-0.2715` n `20`; unknown avg `226.6369` n `1073`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
