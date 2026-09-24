# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T16:07:33.566064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.768` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5612` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0925` n `12`; crypto_alt avg `-0.2398` n `234`; crypto_major avg `-0.2508` n `8`; equity avg `-0.1982` n `141`; fx avg `0.0089` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0479` n `20`; unknown avg `-0.2265` n `929`
- 1h: commodity avg `0.2642` n `12`; crypto_alt avg `0.7458` n `234`; crypto_major avg `0.5253` n `8`; equity avg `-0.037` n `141`; fx avg `0.0106` n `6`; index avg `-0.0118` n `26`; metal avg `0.0306` n `20`; unknown avg `0.8806` n `929`
- 4h: commodity avg `0.9154` n `12`; crypto_alt avg `3.0658` n `234`; crypto_major avg `1.6528` n `8`; equity avg `0.0916` n `141`; fx avg `0.028` n `6`; index avg `-0.0307` n `26`; metal avg `-0.1152` n `20`; unknown avg `1.66` n `883`
- 24h: commodity avg `1.2678` n `12`; crypto_alt avg `2.5884` n `234`; crypto_major avg `0.5302` n `8`; equity avg `-1.3933` n `141`; fx avg `0.0409` n `6`; index avg `-0.253` n `26`; metal avg `-0.2283` n `20`; unknown avg `262.5531` n `825`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
