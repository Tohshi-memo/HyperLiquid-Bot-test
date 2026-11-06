# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T01:22:25.620121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0818` n `13`; crypto_alt avg `-0.4001` n `239`; crypto_major avg `-0.421` n `8`; equity avg `-0.3664` n `158`; fx avg `-0.0269` n `6`; index avg `-0.0517` n `27`; metal avg `-0.0636` n `20`; unknown avg `68.7276` n `1256`
- 1h: commodity avg `0.1216` n `13`; crypto_alt avg `0.133` n `239`; crypto_major avg `-0.072` n `8`; equity avg `0.1249` n `158`; fx avg `-0.0287` n `6`; index avg `-0.017` n `27`; metal avg `-0.1168` n `20`; unknown avg `21.9218` n `1254`
- 4h: commodity avg `0.1156` n `13`; crypto_alt avg `0.2292` n `239`; crypto_major avg `0.0451` n `8`; equity avg `0.8741` n `158`; fx avg `-0.0134` n `6`; index avg `0.0723` n `27`; metal avg `-0.0387` n `20`; unknown avg `0.3901` n `1214`
- 24h: commodity avg `1.1935` n `13`; crypto_alt avg `-4.2498` n `239`; crypto_major avg `-5.2173` n `8`; equity avg `-6.3622` n `158`; fx avg `0.0727` n `6`; index avg `-0.8946` n `27`; metal avg `-0.2622` n `20`; unknown avg `230.8016` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2319`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
