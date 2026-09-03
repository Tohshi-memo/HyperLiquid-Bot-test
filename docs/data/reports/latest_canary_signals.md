# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T08:22:27.919161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1638` n `12`; crypto_alt avg `-0.2753` n `232`; crypto_major avg `-0.3304` n `8`; equity avg `-0.1501` n `133`; fx avg `0.0018` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0665` n `20`; unknown avg `0.185` n `792`
- 1h: commodity avg `0.0202` n `12`; crypto_alt avg `-0.0199` n `232`; crypto_major avg `-0.1513` n `8`; equity avg `0.0982` n `133`; fx avg `0.0346` n `6`; index avg `0.0469` n `26`; metal avg `0.0951` n `20`; unknown avg `3.7268` n `790`
- 4h: commodity avg `-0.1247` n `12`; crypto_alt avg `0.5397` n `232`; crypto_major avg `0.3361` n `8`; equity avg `-0.2651` n `133`; fx avg `-0.0735` n `6`; index avg `-0.0827` n `26`; metal avg `0.0584` n `20`; unknown avg `-0.0203` n `754`
- 24h: commodity avg `0.1321` n `12`; crypto_alt avg `0.7812` n `232`; crypto_major avg `0.8826` n `8`; equity avg `1.4839` n `133`; fx avg `-0.3556` n `6`; index avg `0.1345` n `26`; metal avg `0.824` n `20`; unknown avg `-0.2922` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0428`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0407`, n `668`, weak_sample_signal
