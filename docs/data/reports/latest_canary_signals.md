# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T08:07:28.580358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.1002` n `230`; crypto_major avg `0.0623` n `8`; equity avg `0.0217` n `113`; fx avg `-0.0003` n `6`; index avg `0.0039` n `25`; metal avg `0.1016` n `20`; unknown avg `-0.0184` n `785`
- 1h: commodity avg `0.1105` n `12`; crypto_alt avg `-0.1197` n `230`; crypto_major avg `0.1045` n `8`; equity avg `0.1468` n `113`; fx avg `-0.0122` n `6`; index avg `0.025` n `25`; metal avg `0.0703` n `20`; unknown avg `0.0266` n `785`
- 4h: commodity avg `0.3819` n `12`; crypto_alt avg `-0.5485` n `230`; crypto_major avg `-0.2075` n `8`; equity avg `-0.2978` n `113`; fx avg `0.0068` n `6`; index avg `-0.0634` n `25`; metal avg `-0.2738` n `20`; unknown avg `-0.0049` n `753`
- 24h: commodity avg `1.2308` n `12`; crypto_alt avg `-1.4155` n `230`; crypto_major avg `-1.0789` n `8`; equity avg `-1.48` n `113`; fx avg `0.035` n `6`; index avg `-0.0713` n `25`; metal avg `0.1247` n `20`; unknown avg `0.0969` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
