# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:07:37.494486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.0108` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.96` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.8458` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `-0.178` n `230`; crypto_major avg `-0.1858` n `8`; equity avg `0.0125` n `121`; fx avg `0.0013` n `6`; index avg `0.0002` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.0632` n `793`
- 1h: commodity avg `0.0251` n `12`; crypto_alt avg `-0.0583` n `230`; crypto_major avg `-0.1441` n `8`; equity avg `0.0086` n `121`; fx avg `-0.0043` n `6`; index avg `0.0075` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.2052` n `793`
- 4h: commodity avg `0.0192` n `12`; crypto_alt avg `2.9669` n `230`; crypto_major avg `3.9792` n `8`; equity avg `0.1334` n `121`; fx avg `-0.0065` n `6`; index avg `0.0079` n `25`; metal avg `-0.0316` n `20`; unknown avg `-0.0238` n `793`
- 24h: commodity avg `0.1806` n `12`; crypto_alt avg `8.7068` n `230`; crypto_major avg `8.2216` n `8`; equity avg `0.995` n `121`; fx avg `-0.093` n `6`; index avg `0.1088` n `25`; metal avg `0.4472` n `20`; unknown avg `1.4175` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
