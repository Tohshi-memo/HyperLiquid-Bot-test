# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T23:37:35.927650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `13`; crypto_alt avg `-0.0092` n `239`; crypto_major avg `0.1015` n `8`; equity avg `-0.671` n `158`; fx avg `-0.0059` n `6`; index avg `-0.0427` n `27`; metal avg `0.0073` n `20`; unknown avg `49.5287` n `1258`
- 1h: commodity avg `-0.0289` n `13`; crypto_alt avg `-0.5908` n `239`; crypto_major avg `-0.3645` n `8`; equity avg `-1.0183` n `158`; fx avg `-0.013` n `6`; index avg `-0.083` n `27`; metal avg `0.0066` n `20`; unknown avg `48.0048` n `1220`
- 4h: commodity avg `0.1077` n `13`; crypto_alt avg `-1.498` n `239`; crypto_major avg `-0.8759` n `8`; equity avg `-1.9303` n `158`; fx avg `-0.0188` n `6`; index avg `-0.3202` n `27`; metal avg `-0.1828` n `20`; unknown avg `6.0944` n `1162`
- 24h: commodity avg `0.9654` n `13`; crypto_alt avg `-5.8464` n `239`; crypto_major avg `-6.0816` n `8`; equity avg `-9.3491` n `158`; fx avg `0.0567` n `6`; index avg `-1.3723` n `27`; metal avg `0.0444` n `20`; unknown avg `232.8593` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2367`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1911`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1756`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1637`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.161`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `669`, weak_sample_signal
