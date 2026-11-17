# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T15:22:28.961295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0802` n `13`; crypto_alt avg `0.4285` n `239`; crypto_major avg `0.5548` n `8`; equity avg `-0.1229` n `162`; fx avg `0.0094` n `6`; index avg `-0.0159` n `27`; metal avg `0.0462` n `20`; unknown avg `0.8748` n `1264`
- 1h: commodity avg `-0.1165` n `13`; crypto_alt avg `-0.186` n `239`; crypto_major avg `-0.304` n `8`; equity avg `-1.1363` n `162`; fx avg `0.0004` n `6`; index avg `-0.0972` n `27`; metal avg `0.0088` n `20`; unknown avg `0.6383` n `1264`
- 4h: commodity avg `0.0771` n `13`; crypto_alt avg `0.455` n `239`; crypto_major avg `0.6392` n `8`; equity avg `-0.4357` n `162`; fx avg `0.0376` n `6`; index avg `-0.0678` n `27`; metal avg `-0.0174` n `20`; unknown avg `10.5016` n `1218`
- 24h: commodity avg `-0.1742` n `13`; crypto_alt avg `1.6393` n `239`; crypto_major avg `1.9726` n `8`; equity avg `-1.3292` n `162`; fx avg `-0.0373` n `6`; index avg `-0.1836` n `27`; metal avg `0.0365` n `20`; unknown avg `18.0108` n `1107`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
