# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T14:22:29.943778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4433` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1706` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5224` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0153` n `12`; crypto_alt avg `0.1429` n `230`; crypto_major avg `0.1613` n `8`; equity avg `0.115` n `92`; fx avg `-0.0099` n `6`; index avg `-0.0035` n `25`; metal avg `0.0501` n `20`; unknown avg `-0.0557` n `766`
- 1h: commodity avg `-0.1484` n `12`; crypto_alt avg `-0.2769` n `230`; crypto_major avg `-0.3165` n `8`; equity avg `-0.6854` n `92`; fx avg `0.0106` n `6`; index avg `-0.0368` n `25`; metal avg `0.1542` n `20`; unknown avg `-0.0105` n `766`
- 4h: commodity avg `-0.2912` n `12`; crypto_alt avg `1.4854` n `230`; crypto_major avg `2.1521` n `8`; equity avg `-0.0185` n `92`; fx avg `0.0083` n `6`; index avg `0.1809` n `25`; metal avg `0.6297` n `20`; unknown avg `0.8755` n `766`
- 24h: commodity avg `0.9113` n `12`; crypto_alt avg `0.8354` n `230`; crypto_major avg `2.2482` n `8`; equity avg `0.138` n `92`; fx avg `-0.0111` n `6`; index avg `0.1246` n `25`; metal avg `0.6664` n `20`; unknown avg `-0.1472` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
