# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T00:24:19.226621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.719` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.7024` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.6062` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.7245` n `230`; crypto_major avg `0.8207` n `8`; equity avg `0.0582` n `121`; fx avg `0.002` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0109` n `20`; unknown avg `-0.1905` n `793`
- 1h: commodity avg `-0.0301` n `12`; crypto_alt avg `0.0233` n `230`; crypto_major avg `-0.9872` n `8`; equity avg `0.0592` n `121`; fx avg `0.0018` n `6`; index avg `0.003` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.1572` n `793`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `2.4369` n `230`; crypto_major avg `2.6967` n `8`; equity avg `0.0905` n `121`; fx avg `-0.0003` n `6`; index avg `0.0271` n `25`; metal avg `-0.0223` n `20`; unknown avg `-0.1215` n `793`
- 24h: commodity avg `0.1705` n `12`; crypto_alt avg `8.383` n `230`; crypto_major avg `6.6476` n `8`; equity avg `0.7971` n `121`; fx avg `-0.0125` n `6`; index avg `0.1029` n `25`; metal avg `0.458` n `20`; unknown avg `1.2556` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
