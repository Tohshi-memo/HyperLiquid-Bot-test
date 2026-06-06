# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T16:37:26.170746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0206` n `12`; crypto_alt avg `-0.2204` n `228`; crypto_major avg `-0.2406` n `8`; equity avg `-0.0444` n `74`; fx avg `-0.0036` n `6`; index avg `-0.002` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.4866` n `515`
- 1h: commodity avg `0.0388` n `12`; crypto_alt avg `-0.4657` n `228`; crypto_major avg `-0.5376` n `8`; equity avg `0.0604` n `74`; fx avg `0.0459` n `6`; index avg `0.0445` n `23`; metal avg `0.0538` n `18`; unknown avg `-3.5711` n `515`
- 4h: commodity avg `0.1364` n `12`; crypto_alt avg `-0.0509` n `228`; crypto_major avg `-0.433` n `8`; equity avg `0.0887` n `74`; fx avg `0.0407` n `6`; index avg `0.2152` n `23`; metal avg `-0.1383` n `18`; unknown avg `-0.5607` n `415`
- 24h: commodity avg `0.4733` n `12`; crypto_alt avg `-1.2877` n `228`; crypto_major avg `-1.2569` n `8`; equity avg `-2.123` n `74`; fx avg `-0.0325` n `6`; index avg `-1.2428` n `23`; metal avg `-1.0877` n `18`; unknown avg `0.9301` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
