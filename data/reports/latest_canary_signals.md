# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T17:37:32.386788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0638` n `12`; crypto_alt avg `0.1872` n `230`; crypto_major avg `0.251` n `8`; equity avg `0.1798` n `113`; fx avg `0.0025` n `6`; index avg `0.0099` n `25`; metal avg `-0.0022` n `20`; unknown avg `0.0935` n `786`
- 1h: commodity avg `0.0387` n `12`; crypto_alt avg `0.1906` n `230`; crypto_major avg `0.1407` n `8`; equity avg `0.2343` n `113`; fx avg `0.0132` n `6`; index avg `0.0238` n `25`; metal avg `-0.0468` n `20`; unknown avg `0.0996` n `786`
- 4h: commodity avg `0.0951` n `12`; crypto_alt avg `-0.3751` n `230`; crypto_major avg `-0.0734` n `8`; equity avg `0.939` n `113`; fx avg `0.015` n `6`; index avg `0.0344` n `25`; metal avg `-0.1353` n `20`; unknown avg `0.1389` n `786`
- 24h: commodity avg `0.061` n `12`; crypto_alt avg `-0.0093` n `230`; crypto_major avg `0.9721` n `8`; equity avg `3.8365` n `113`; fx avg `0.0482` n `6`; index avg `0.4092` n `25`; metal avg `0.2004` n `20`; unknown avg `0.1542` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2279`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1963`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
