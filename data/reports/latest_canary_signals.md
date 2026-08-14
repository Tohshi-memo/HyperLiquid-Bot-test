# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T14:37:30.426424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `0.0013` n `230`; crypto_major avg `0.1431` n `8`; equity avg `0.1556` n `114`; fx avg `-0.018` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.0773` n `786`
- 1h: commodity avg `0.2326` n `12`; crypto_alt avg `-0.0585` n `230`; crypto_major avg `-0.0149` n `8`; equity avg `0.3928` n `114`; fx avg `0.0317` n `6`; index avg `0.0101` n `25`; metal avg `0.0301` n `20`; unknown avg `-0.2047` n `786`
- 4h: commodity avg `0.0789` n `12`; crypto_alt avg `-0.0683` n `230`; crypto_major avg `-0.3112` n `8`; equity avg `-0.0698` n `114`; fx avg `0.0346` n `6`; index avg `-0.0556` n `25`; metal avg `0.2466` n `20`; unknown avg `2.9555` n `786`
- 24h: commodity avg `0.2286` n `12`; crypto_alt avg `-1.1049` n `230`; crypto_major avg `-1.4688` n `8`; equity avg `-0.1578` n `114`; fx avg `0.0225` n `6`; index avg `-0.0261` n `25`; metal avg `0.1504` n `20`; unknown avg `0.2839` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1982`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
