# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T15:37:30.774845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0997` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0913` n `12`; crypto_alt avg `-0.711` n `230`; crypto_major avg `-0.5123` n `8`; equity avg `-0.1849` n `113`; fx avg `0.0034` n `6`; index avg `-0.0307` n `25`; metal avg `-0.0802` n `20`; unknown avg `-0.1595` n `785`
- 1h: commodity avg `0.091` n `12`; crypto_alt avg `-1.2091` n `230`; crypto_major avg `-0.6734` n `8`; equity avg `-0.0803` n `113`; fx avg `0.0042` n `6`; index avg `-0.0406` n `25`; metal avg `-0.1299` n `20`; unknown avg `-0.1646` n `785`
- 4h: commodity avg `0.1616` n `12`; crypto_alt avg `-1.5246` n `230`; crypto_major avg `-1.1269` n `8`; equity avg `0.186` n `113`; fx avg `0.0156` n `6`; index avg `-0.0272` n `25`; metal avg `-0.2111` n `20`; unknown avg `-0.0042` n `785`
- 24h: commodity avg `0.1799` n `12`; crypto_alt avg `-2.1459` n `230`; crypto_major avg `-0.6263` n `8`; equity avg `0.2106` n `113`; fx avg `-0.0488` n `6`; index avg `0.1142` n `25`; metal avg `0.0738` n `20`; unknown avg `-0.2931` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
