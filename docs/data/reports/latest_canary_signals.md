# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T12:52:28.029069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0856` n `12`; crypto_alt avg `-0.0386` n `230`; crypto_major avg `-0.0324` n `8`; equity avg `-0.0873` n `113`; fx avg `-0.003` n `6`; index avg `-0.0208` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.0179` n `785`
- 1h: commodity avg `0.2005` n `12`; crypto_alt avg `-0.233` n `230`; crypto_major avg `-0.0917` n `8`; equity avg `-0.0179` n `113`; fx avg `0.0287` n `6`; index avg `0.0091` n `25`; metal avg `-0.1317` n `20`; unknown avg `-0.0825` n `785`
- 4h: commodity avg `-0.2601` n `12`; crypto_alt avg `-0.1504` n `230`; crypto_major avg `0.3177` n `8`; equity avg `0.5274` n `113`; fx avg `-0.0521` n `6`; index avg `0.0992` n `25`; metal avg `-0.0312` n `20`; unknown avg `-0.2184` n `785`
- 24h: commodity avg `0.652` n `12`; crypto_alt avg `-1.3947` n `230`; crypto_major avg `-0.301` n `8`; equity avg `-0.1911` n `113`; fx avg `-0.0197` n `6`; index avg `0.1654` n `25`; metal avg `0.2874` n `20`; unknown avg `0.0183` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1946`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
