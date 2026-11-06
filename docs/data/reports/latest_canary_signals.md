# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T19:07:32.806215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.045` n `13`; crypto_alt avg `0.0276` n `239`; crypto_major avg `-0.0616` n `8`; equity avg `0.0486` n `158`; fx avg `0.0012` n `6`; index avg `-0.0046` n `27`; metal avg `-0.0118` n `20`; unknown avg `1.0795` n `1257`
- 1h: commodity avg `0.1581` n `13`; crypto_alt avg `0.0804` n `239`; crypto_major avg `0.079` n `8`; equity avg `0.6182` n `158`; fx avg `0.02` n `6`; index avg `0.0623` n `27`; metal avg `0.0922` n `20`; unknown avg `0.7032` n `1253`
- 4h: commodity avg `0.0949` n `13`; crypto_alt avg `-0.2828` n `239`; crypto_major avg `0.2139` n `8`; equity avg `-0.0738` n `158`; fx avg `-0.0006` n `6`; index avg `-0.0307` n `27`; metal avg `0.1619` n `20`; unknown avg `25.4236` n `1245`
- 24h: commodity avg `0.2052` n `13`; crypto_alt avg `1.8586` n `239`; crypto_major avg `-0.0797` n `8`; equity avg `2.332` n `158`; fx avg `-0.0956` n `6`; index avg `0.2383` n `27`; metal avg `-0.0933` n `20`; unknown avg `46.1515` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
