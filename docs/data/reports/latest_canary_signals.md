# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T00:52:26.704772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `13`; crypto_alt avg `-0.1721` n `239`; crypto_major avg `-0.0516` n `8`; equity avg `-0.3438` n `158`; fx avg `0.0046` n `6`; index avg `-0.085` n `27`; metal avg `-0.0205` n `20`; unknown avg `1.7284` n `1256`
- 1h: commodity avg `-0.0666` n `13`; crypto_alt avg `1.253` n `239`; crypto_major avg `0.8239` n `8`; equity avg `2.1532` n `158`; fx avg `0.0229` n `6`; index avg `0.2031` n `27`; metal avg `0.119` n `20`; unknown avg `1.6356` n `1246`
- 4h: commodity avg `0.0023` n `13`; crypto_alt avg `-0.4645` n `239`; crypto_major avg `-0.4637` n `8`; equity avg `0.2013` n `158`; fx avg `0.0089` n `6`; index avg `-0.0748` n `27`; metal avg `-0.0612` n `20`; unknown avg `7.3492` n `1208`
- 24h: commodity avg `0.9601` n `13`; crypto_alt avg `-4.6226` n `239`; crypto_major avg `-5.5021` n `8`; equity avg `-7.0338` n `158`; fx avg `0.1127` n `6`; index avg `-1.0696` n `27`; metal avg `-0.0564` n `20`; unknown avg `232.5266` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2312`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
