# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T00:11:09.260580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0483` n `13`; crypto_alt avg `0.3827` n `239`; crypto_major avg `0.2958` n `8`; equity avg `1.1294` n `158`; fx avg `0.0082` n `6`; index avg `0.1419` n `27`; metal avg `0.0978` n `20`; unknown avg `1.127` n `1244`
- 1h: commodity avg `-0.0799` n `13`; crypto_alt avg `0.4009` n `239`; crypto_major avg `0.3943` n `8`; equity avg `0.4865` n `158`; fx avg `0.0107` n `6`; index avg `0.0889` n `27`; metal avg `0.0813` n `20`; unknown avg `48.4938` n `1246`
- 4h: commodity avg `0.0365` n `13`; crypto_alt avg `-1.3382` n `239`; crypto_major avg `-0.7581` n `8`; equity avg `-1.03` n `158`; fx avg `-0.0188` n `6`; index avg `-0.2013` n `27`; metal avg `-0.1313` n `20`; unknown avg `20.3578` n `1178`
- 24h: commodity avg `0.8835` n `13`; crypto_alt avg `-5.1948` n `239`; crypto_major avg `-5.647` n `8`; equity avg `-8.0432` n `158`; fx avg `0.0661` n `6`; index avg `-1.1714` n `27`; metal avg `0.1215` n `20`; unknown avg `233.097` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.235`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1908`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1786`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1769`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.167`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1616`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1615`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `669`, weak_sample_signal
