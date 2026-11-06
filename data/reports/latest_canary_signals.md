# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T12:22:24.060798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0484` n `13`; crypto_alt avg `0.1357` n `239`; crypto_major avg `-0.0103` n `8`; equity avg `-0.2569` n `158`; fx avg `0.0281` n `6`; index avg `-0.0222` n `27`; metal avg `0.0369` n `20`; unknown avg `0.3459` n `1255`
- 1h: commodity avg `-0.066` n `13`; crypto_alt avg `0.315` n `239`; crypto_major avg `0.3246` n `8`; equity avg `0.4946` n `158`; fx avg `0.049` n `6`; index avg `0.0305` n `27`; metal avg `0.0719` n `20`; unknown avg `0.1214` n `1189`
- 4h: commodity avg `0.0254` n `13`; crypto_alt avg `0.956` n `239`; crypto_major avg `0.8012` n `8`; equity avg `1.7084` n `158`; fx avg `0.094` n `6`; index avg `0.1848` n `27`; metal avg `0.0092` n `20`; unknown avg `32.5213` n `1176`
- 24h: commodity avg `0.6174` n `13`; crypto_alt avg `-2.2782` n `239`; crypto_major avg `-4.6301` n `8`; equity avg `-3.7729` n `158`; fx avg `0.0133` n `6`; index avg `-0.5643` n `27`; metal avg `-0.3053` n `20`; unknown avg `15.0565` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
