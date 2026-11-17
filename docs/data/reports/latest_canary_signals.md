# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T21:07:28.790624+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `13`; crypto_alt avg `0.1643` n `239`; crypto_major avg `0.2084` n `8`; equity avg `0.6428` n `163`; fx avg `-0.003` n `6`; index avg `0.0893` n `27`; metal avg `0.0447` n `20`; unknown avg `0.0612` n `1243`
- 1h: commodity avg `0.1031` n `13`; crypto_alt avg `0.4581` n `239`; crypto_major avg `0.3583` n `8`; equity avg `0.81` n `163`; fx avg `-0.005` n `6`; index avg `0.098` n `27`; metal avg `0.0337` n `20`; unknown avg `0.9583` n `1247`
- 4h: commodity avg `-0.0216` n `13`; crypto_alt avg `0.4924` n `239`; crypto_major avg `0.5782` n `8`; equity avg `0.542` n `163`; fx avg `-0.0172` n `6`; index avg `0.0605` n `27`; metal avg `-0.1311` n `20`; unknown avg `20.0874` n `1235`
- 24h: commodity avg `0.1911` n `13`; crypto_alt avg `0.1554` n `239`; crypto_major avg `0.092` n `8`; equity avg `-0.9344` n `163`; fx avg `0.0382` n `6`; index avg `-0.0999` n `27`; metal avg `-0.0149` n `20`; unknown avg `6.0271` n `1107`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
