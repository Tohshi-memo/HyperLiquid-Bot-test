# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T04:37:29.732078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.2652` n `234`; crypto_major avg `0.1147` n `8`; equity avg `0.1028` n `141`; fx avg `-0.007` n `6`; index avg `0.0187` n `26`; metal avg `0.0272` n `20`; unknown avg `2.5477` n `945`
- 1h: commodity avg `0.0399` n `12`; crypto_alt avg `0.2701` n `234`; crypto_major avg `-0.0434` n `8`; equity avg `-0.1148` n `141`; fx avg `-0.0097` n `6`; index avg `-0.0111` n `26`; metal avg `0.0502` n `20`; unknown avg `0.2933` n `937`
- 4h: commodity avg `0.0317` n `12`; crypto_alt avg `0.7566` n `234`; crypto_major avg `-0.4751` n `8`; equity avg `-0.4213` n `141`; fx avg `0.0305` n `6`; index avg `-0.0448` n `26`; metal avg `0.0326` n `20`; unknown avg `2.1239` n `937`
- 24h: commodity avg `0.5415` n `12`; crypto_alt avg `-4.6223` n `234`; crypto_major avg `-5.0886` n `8`; equity avg `-2.051` n `140`; fx avg `0.1292` n `6`; index avg `-0.3737` n `26`; metal avg `-0.6595` n `20`; unknown avg `585.4814` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
