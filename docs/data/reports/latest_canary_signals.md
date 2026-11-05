# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T20:07:34.919907+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0296` n `13`; crypto_alt avg `-0.2037` n `239`; crypto_major avg `-0.2905` n `8`; equity avg `-0.8819` n `158`; fx avg `0.0002` n `6`; index avg `-0.1023` n `27`; metal avg `-0.1298` n `20`; unknown avg `1.8624` n `1228`
- 1h: commodity avg `0.1526` n `13`; crypto_alt avg `0.9744` n `239`; crypto_major avg `0.4805` n `8`; equity avg `0.7918` n `158`; fx avg `0.0083` n `6`; index avg `0.0516` n `27`; metal avg `0.0227` n `20`; unknown avg `2.0972` n `1232`
- 4h: commodity avg `0.0725` n `13`; crypto_alt avg `1.5842` n `239`; crypto_major avg `-0.0931` n `8`; equity avg `1.3905` n `158`; fx avg `0.0124` n `6`; index avg `-0.0476` n `27`; metal avg `0.1447` n `20`; unknown avg `7.4561` n `1234`
- 24h: commodity avg `0.7458` n `13`; crypto_alt avg `-3.4236` n `239`; crypto_major avg `-4.5616` n `8`; equity avg `-7.2754` n `158`; fx avg `0.0955` n `6`; index avg `-1.0253` n `27`; metal avg `0.2135` n `20`; unknown avg `218.8587` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2289`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
