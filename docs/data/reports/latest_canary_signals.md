# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T02:22:27.700758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.12` n `13`; crypto_alt avg `0.0535` n `239`; crypto_major avg `-0.0618` n `8`; equity avg `0.4728` n `158`; fx avg `-0.0052` n `6`; index avg `0.0589` n `27`; metal avg `-0.0908` n `20`; unknown avg `1.4167` n `1263`
- 1h: commodity avg `0.0153` n `13`; crypto_alt avg `0.874` n `239`; crypto_major avg `0.6422` n `8`; equity avg `1.4565` n `158`; fx avg `0.0346` n `6`; index avg `0.2408` n `27`; metal avg `0.1112` n `20`; unknown avg `0.6207` n `1256`
- 4h: commodity avg `-0.1691` n `13`; crypto_alt avg `-0.1045` n `239`; crypto_major avg `0.1589` n `8`; equity avg `-0.5868` n `158`; fx avg `0.0315` n `6`; index avg `-0.1391` n `27`; metal avg `0.3963` n `20`; unknown avg `20.6489` n `1196`
- 24h: commodity avg `-1.6499` n `13`; crypto_alt avg `3.403` n `239`; crypto_major avg `4.0014` n `8`; equity avg `0.6962` n `158`; fx avg `0.1286` n `6`; index avg `0.4286` n `27`; metal avg `1.7261` n `20`; unknown avg `31.7689` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2558`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
