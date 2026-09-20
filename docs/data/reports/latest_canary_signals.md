# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T17:52:25.478248+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5869` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.0811` n `234`; crypto_major avg `0.0006` n `8`; equity avg `0.0099` n `140`; fx avg `0.0065` n `6`; index avg `0.0047` n `26`; metal avg `0.0198` n `20`; unknown avg `0.7385` n `943`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.0465` n `234`; crypto_major avg `-0.1455` n `8`; equity avg `0.0219` n `140`; fx avg `-0.0237` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0059` n `20`; unknown avg `16.3628` n `929`
- 4h: commodity avg `0.0138` n `12`; crypto_alt avg `2.8068` n `234`; crypto_major avg `1.6117` n `8`; equity avg `0.31` n `140`; fx avg `0.0089` n `6`; index avg `0.0356` n `26`; metal avg `0.0248` n `20`; unknown avg `1.2426` n `879`
- 24h: commodity avg `0.3855` n `12`; crypto_alt avg `0.1859` n `234`; crypto_major avg `-0.7669` n `8`; equity avg `-0.0121` n `140`; fx avg `-0.0315` n `6`; index avg `-0.0262` n `26`; metal avg `-0.003` n `20`; unknown avg `120.0665` n `827`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
