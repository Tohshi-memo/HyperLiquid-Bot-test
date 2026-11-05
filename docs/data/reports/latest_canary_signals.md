# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T20:37:30.770213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `13`; crypto_alt avg `-0.0431` n `239`; crypto_major avg `0.0409` n `8`; equity avg `-0.4561` n `158`; fx avg `-0.0039` n `6`; index avg `-0.078` n `27`; metal avg `-0.079` n `20`; unknown avg `34.7705` n `1256`
- 1h: commodity avg `-0.0479` n `13`; crypto_alt avg `0.085` n `239`; crypto_major avg `0.1738` n `8`; equity avg `-0.3532` n `158`; fx avg `0.0102` n `6`; index avg `-0.0964` n `27`; metal avg `-0.0751` n `20`; unknown avg `31.2544` n `1232`
- 4h: commodity avg `0.1663` n `13`; crypto_alt avg `0.4375` n `239`; crypto_major avg `-0.8362` n `8`; equity avg `-1.738` n `158`; fx avg `-0.0005` n `6`; index avg `-0.3323` n `27`; metal avg `-0.2686` n `20`; unknown avg `2.2208` n `1234`
- 24h: commodity avg `0.7051` n `13`; crypto_alt avg `-3.9383` n `239`; crypto_major avg `-4.7687` n `8`; equity avg `-7.8785` n `158`; fx avg `0.0816` n `6`; index avg `-1.1343` n `27`; metal avg `0.0962` n `20`; unknown avg `36.0119` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.23`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1751`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
