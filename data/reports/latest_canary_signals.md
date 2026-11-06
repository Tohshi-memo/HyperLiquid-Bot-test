# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T12:52:30.989181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0737` n `13`; crypto_alt avg `-0.1497` n `239`; crypto_major avg `-0.3236` n `8`; equity avg `-0.2644` n `158`; fx avg `-0.0061` n `6`; index avg `-0.0169` n `27`; metal avg `-0.0348` n `20`; unknown avg `1.4263` n `1257`
- 1h: commodity avg `-0.1397` n `13`; crypto_alt avg `-0.1889` n `239`; crypto_major avg `-0.3486` n `8`; equity avg `-0.3536` n `158`; fx avg `0.017` n `6`; index avg `-0.0347` n `27`; metal avg `-0.0487` n `20`; unknown avg `4.938` n `1229`
- 4h: commodity avg `-0.0454` n `13`; crypto_alt avg `0.7069` n `239`; crypto_major avg `0.4596` n `8`; equity avg `1.2473` n `158`; fx avg `0.0504` n `6`; index avg `0.1061` n `27`; metal avg `-0.0754` n `20`; unknown avg `5.6543` n `1176`
- 24h: commodity avg `0.4473` n `13`; crypto_alt avg `-2.1303` n `239`; crypto_major avg `-4.4644` n `8`; equity avg `-3.5038` n `158`; fx avg `-0.0025` n `6`; index avg `-0.5548` n `27`; metal avg `-0.3549` n `20`; unknown avg `10.3993` n `1079`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
