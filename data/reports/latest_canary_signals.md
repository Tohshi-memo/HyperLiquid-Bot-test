# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T20:37:32.275246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-0.2892` n `234`; crypto_major avg `-0.1415` n `8`; equity avg `0.033` n `141`; fx avg `-0.0018` n `6`; index avg `0.0054` n `26`; metal avg `-0.0006` n `20`; unknown avg `1.6469` n `942`
- 1h: commodity avg `-0.1676` n `12`; crypto_alt avg `-0.4275` n `234`; crypto_major avg `-0.2874` n `8`; equity avg `-0.1151` n `141`; fx avg `-0.0092` n `6`; index avg `-0.0372` n `26`; metal avg `-0.0623` n `20`; unknown avg `4.9246` n `876`
- 4h: commodity avg `0.3071` n `12`; crypto_alt avg `-0.4262` n `234`; crypto_major avg `-0.3599` n `8`; equity avg `-0.2106` n `141`; fx avg `0.0031` n `6`; index avg `-0.0868` n `26`; metal avg `-0.1013` n `20`; unknown avg `7.5408` n `869`
- 24h: commodity avg `0.7818` n `12`; crypto_alt avg `3.9369` n `234`; crypto_major avg `1.5322` n `8`; equity avg `-0.3539` n `141`; fx avg `0.0264` n `6`; index avg `-0.1354` n `26`; metal avg `-0.1289` n `20`; unknown avg `13.3766` n `849`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
