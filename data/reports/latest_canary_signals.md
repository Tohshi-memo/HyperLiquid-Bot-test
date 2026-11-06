# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T00:22:29.682648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `13`; crypto_alt avg `0.4377` n `239`; crypto_major avg `0.2358` n `8`; equity avg `0.512` n `158`; fx avg `0.0094` n `6`; index avg `0.0409` n `27`; metal avg `0.0247` n `20`; unknown avg `0.2506` n `1256`
- 1h: commodity avg `-0.1242` n `13`; crypto_alt avg `0.8412` n `239`; crypto_major avg `0.631` n `8`; equity avg `1.0048` n `158`; fx avg `0.0201` n `6`; index avg `0.1301` n `27`; metal avg `0.1061` n `20`; unknown avg `29.4731` n `1248`
- 4h: commodity avg `0.0113` n `13`; crypto_alt avg `-0.7927` n `239`; crypto_major avg `-0.4837` n `8`; equity avg `-0.3996` n `158`; fx avg `-0.007` n `6`; index avg `-0.1325` n `27`; metal avg `-0.0886` n `20`; unknown avg `12.8836` n `1178`
- 24h: commodity avg `0.8837` n `13`; crypto_alt avg `-4.9199` n `239`; crypto_major avg `-5.7598` n `8`; equity avg `-7.679` n `158`; fx avg `0.0644` n `6`; index avg `-1.12` n `27`; metal avg `0.0369` n `20`; unknown avg `233.2931` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
