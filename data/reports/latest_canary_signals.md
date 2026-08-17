# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T02:56:32.796987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0905` n `12`; crypto_alt avg `0.1547` n `230`; crypto_major avg `0.2484` n `8`; equity avg `0.217` n `114`; fx avg `0.0336` n `6`; index avg `0.0131` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.1261` n `792`
- 1h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.3945` n `230`; crypto_major avg `0.4094` n `8`; equity avg `0.4092` n `114`; fx avg `0.0424` n `6`; index avg `0.0265` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.1886` n `792`
- 4h: commodity avg `-0.0428` n `12`; crypto_alt avg `0.9024` n `230`; crypto_major avg `1.1932` n `8`; equity avg `0.5228` n `114`; fx avg `-0.0071` n `6`; index avg `0.0171` n `25`; metal avg `0.1148` n `20`; unknown avg `1.1155` n `791`
- 24h: commodity avg `-0.1159` n `12`; crypto_alt avg `0.4651` n `230`; crypto_major avg `0.667` n `8`; equity avg `0.7273` n `114`; fx avg `-0.0167` n `6`; index avg `0.0605` n `25`; metal avg `0.2075` n `20`; unknown avg `0.1146` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1474`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
