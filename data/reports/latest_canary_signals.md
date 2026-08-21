# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T22:37:26.089986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.2897` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.2822` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.0347` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0039` n `230`; crypto_major avg `0.0645` n `8`; equity avg `-0.0005` n `121`; fx avg `-0.0005` n `6`; index avg `0.0067` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.3443` n `793`
- 1h: commodity avg `0.0262` n `12`; crypto_alt avg `0.7217` n `230`; crypto_major avg `1.221` n `8`; equity avg `0.0335` n `121`; fx avg `-0.0067` n `6`; index avg `0.0153` n `25`; metal avg `-0.0198` n `20`; unknown avg `1.2133` n `793`
- 4h: commodity avg `-0.0439` n `12`; crypto_alt avg `1.8816` n `230`; crypto_major avg `3.2383` n `8`; equity avg `0.2036` n `121`; fx avg `-0.0031` n `6`; index avg `0.0156` n `25`; metal avg `-0.0514` n `20`; unknown avg `1.0503` n `793`
- 24h: commodity avg `0.1713` n `12`; crypto_alt avg `8.8852` n `230`; crypto_major avg `8.255` n `8`; equity avg `0.9664` n `121`; fx avg `-0.0817` n `6`; index avg `0.124` n `25`; metal avg `0.4903` n `20`; unknown avg `2.5697` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
