# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T08:37:26.668406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.63` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.0753` n `233`; crypto_major avg `0.0084` n `8`; equity avg `0.0025` n `136`; fx avg `0.0` n `6`; index avg `0.0067` n `26`; metal avg `0.0024` n `20`; unknown avg `0.2666` n `832`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.0274` n `233`; crypto_major avg `0.1091` n `8`; equity avg `0.0039` n `136`; fx avg `0.0043` n `6`; index avg `-0.0017` n `26`; metal avg `0.0037` n `20`; unknown avg `0.8038` n `830`
- 4h: commodity avg `-0.0321` n `12`; crypto_alt avg `0.4457` n `233`; crypto_major avg `0.1715` n `8`; equity avg `-0.0571` n `136`; fx avg `-0.0017` n `6`; index avg `0.0087` n `26`; metal avg `0.0117` n `20`; unknown avg `0.0537` n `800`
- 24h: commodity avg `-0.2395` n `12`; crypto_alt avg `1.3227` n `233`; crypto_major avg `0.8541` n `8`; equity avg `0.0259` n `136`; fx avg `-0.0795` n `6`; index avg `0.1099` n `26`; metal avg `-0.0823` n `20`; unknown avg `0.8994` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
