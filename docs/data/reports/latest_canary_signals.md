# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T20:22:31.312182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `13`; crypto_alt avg `-0.1174` n `239`; crypto_major avg `-0.0413` n `8`; equity avg `-0.1264` n `158`; fx avg `-0.0025` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0181` n `20`; unknown avg `2.6245` n `1256`
- 1h: commodity avg `0.0494` n `13`; crypto_alt avg `0.3945` n `239`; crypto_major avg `0.1526` n `8`; equity avg `0.1651` n `158`; fx avg `0.0116` n `6`; index avg `-0.0144` n `27`; metal avg `-0.0206` n `20`; unknown avg `4.4556` n `1232`
- 4h: commodity avg `0.1271` n `13`; crypto_alt avg `0.2635` n `239`; crypto_major avg `-1.1137` n `8`; equity avg `-1.2692` n `158`; fx avg `0.0101` n `6`; index avg `-0.2513` n `27`; metal avg `-0.1383` n `20`; unknown avg `6.4072` n `1234`
- 24h: commodity avg `0.6973` n `13`; crypto_alt avg `-3.9025` n `239`; crypto_major avg `-4.8314` n `8`; equity avg `-7.4625` n `158`; fx avg `0.0857` n `6`; index avg `-1.0724` n `27`; metal avg `0.1825` n `20`; unknown avg `201.4606` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2295`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
