# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T21:22:35.361653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0376` n `13`; crypto_alt avg `-0.3797` n `239`; crypto_major avg `-0.2915` n `8`; equity avg `-0.1555` n `158`; fx avg `-0.0069` n `6`; index avg `-0.0445` n `27`; metal avg `0.0086` n `20`; unknown avg `35.1702` n `1256`
- 1h: commodity avg `0.0176` n `13`; crypto_alt avg `-0.8884` n `239`; crypto_major avg `-0.6011` n `8`; equity avg `-1.1196` n `158`; fx avg `-0.0222` n `6`; index avg `-0.2203` n `27`; metal avg `-0.1664` n `20`; unknown avg `32.2476` n `1216`
- 4h: commodity avg `0.1334` n `13`; crypto_alt avg `0.4839` n `239`; crypto_major avg `-0.5742` n `8`; equity avg `-1.1964` n `158`; fx avg `-0.024` n `6`; index avg `-0.3359` n `27`; metal avg `-0.2875` n `20`; unknown avg `5.2911` n `1194`
- 24h: commodity avg `0.8089` n `13`; crypto_alt avg `-4.681` n `239`; crypto_major avg `-5.23` n `8`; equity avg `-8.7154` n `158`; fx avg `0.07` n `6`; index avg `-1.2962` n `27`; metal avg `0.0046` n `20`; unknown avg `226.6252` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
