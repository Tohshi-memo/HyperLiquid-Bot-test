# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T12:07:33.388344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `13`; crypto_alt avg `-0.3384` n `239`; crypto_major avg `-0.2768` n `8`; equity avg `-0.2765` n `158`; fx avg `0.0294` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0241` n `20`; unknown avg `0.1986` n `1243`
- 1h: commodity avg `0.1789` n `13`; crypto_alt avg `-0.3308` n `239`; crypto_major avg `-0.1968` n `8`; equity avg `-0.1805` n `158`; fx avg `0.0184` n `6`; index avg `-0.0092` n `27`; metal avg `0.0255` n `20`; unknown avg `0.3948` n `1245`
- 4h: commodity avg `0.4346` n `13`; crypto_alt avg `-0.2138` n `239`; crypto_major avg `-0.1631` n `8`; equity avg `-0.1418` n `158`; fx avg `0.0418` n `6`; index avg `0.0125` n `27`; metal avg `0.1317` n `20`; unknown avg `201.2118` n `1145`
- 24h: commodity avg `-1.0877` n `13`; crypto_alt avg `0.2126` n `239`; crypto_major avg `1.5005` n `8`; equity avg `-2.7644` n `158`; fx avg `-0.0046` n `6`; index avg `-0.2607` n `27`; metal avg `0.7242` n `20`; unknown avg `215.1786` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2378`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
