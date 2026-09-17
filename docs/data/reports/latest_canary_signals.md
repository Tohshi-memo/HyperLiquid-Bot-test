# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T22:22:31.300168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0405` n `12`; crypto_alt avg `-0.2194` n `234`; crypto_major avg `-0.2548` n `8`; equity avg `-0.0466` n `140`; fx avg `-0.0048` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0012` n `20`; unknown avg `1.4151` n `871`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `-0.2599` n `234`; crypto_major avg `-0.3046` n `8`; equity avg `-0.0818` n `140`; fx avg `0.0135` n `6`; index avg `-0.0252` n `26`; metal avg `0.0004` n `20`; unknown avg `4.7947` n `853`
- 4h: commodity avg `-0.1748` n `12`; crypto_alt avg `-0.3744` n `234`; crypto_major avg `-0.2777` n `8`; equity avg `-0.059` n `140`; fx avg `-0.0071` n `6`; index avg `-0.046` n `26`; metal avg `-0.1287` n `20`; unknown avg `0.2849` n `801`
- 24h: commodity avg `-0.158` n `12`; crypto_alt avg `3.9342` n `234`; crypto_major avg `2.0832` n `8`; equity avg `2.1425` n `138`; fx avg `-0.0035` n `6`; index avg `0.398` n `26`; metal avg `0.5863` n `20`; unknown avg `7264.7805` n `787`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
