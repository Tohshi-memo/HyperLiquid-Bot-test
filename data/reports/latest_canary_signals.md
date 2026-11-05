# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T19:37:36.271917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0653` n `13`; crypto_alt avg `0.266` n `239`; crypto_major avg `0.0197` n `8`; equity avg `0.0615` n `158`; fx avg `-0.0025` n `6`; index avg `0.004` n `27`; metal avg `-0.0245` n `20`; unknown avg `1.0192` n `1256`
- 1h: commodity avg `0.0432` n `13`; crypto_alt avg `0.6738` n `239`; crypto_major avg `0.1023` n `8`; equity avg `0.4298` n `158`; fx avg `-0.0256` n `6`; index avg `0.0016` n `27`; metal avg `-0.0482` n `20`; unknown avg `6.7284` n `1254`
- 4h: commodity avg `0.1985` n `13`; crypto_alt avg `0.2114` n `239`; crypto_major avg `-1.1508` n `8`; equity avg `-1.1356` n `158`; fx avg `0.002` n `6`; index avg `-0.2661` n `27`; metal avg `-0.071` n `20`; unknown avg `8.9381` n `1246`
- 24h: commodity avg `0.8294` n `13`; crypto_alt avg `-3.9909` n `239`; crypto_major avg `-4.963` n `8`; equity avg `-7.6225` n `158`; fx avg `0.1029` n `6`; index avg `-1.0555` n `27`; metal avg `0.2523` n `20`; unknown avg `54.3102` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
