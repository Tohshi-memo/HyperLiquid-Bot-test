# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T11:52:33.993585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0439` n `229`; crypto_major avg `-0.0171` n `8`; equity avg `-0.0347` n `88`; fx avg `0.0044` n `6`; index avg `0.0048` n `25`; metal avg `0.0202` n `20`; unknown avg `0.0307` n `765`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.0285` n `229`; crypto_major avg `0.083` n `8`; equity avg `0.0048` n `88`; fx avg `0.0044` n `6`; index avg `0.0046` n `25`; metal avg `0.018` n `20`; unknown avg `-0.0` n `765`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.4948` n `229`; crypto_major avg `-0.1421` n `8`; equity avg `0.005` n `88`; fx avg `0.0034` n `6`; index avg `-0.0038` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.1051` n `765`
- 24h: commodity avg `-0.0528` n `12`; crypto_alt avg `-1.2117` n `229`; crypto_major avg `-0.5773` n `8`; equity avg `0.2619` n `88`; fx avg `0.0257` n `6`; index avg `0.0422` n `25`; metal avg `0.0946` n `20`; unknown avg `-1.2067` n `725`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
