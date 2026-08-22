# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T05:07:24.368580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.3032` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `4.2784` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `4.1994` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0067` n `12`; crypto_alt avg `-0.5052` n `230`; crypto_major avg `-0.5444` n `8`; equity avg `-0.0428` n `121`; fx avg `-0.0038` n `6`; index avg `-0.007` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.2595` n `794`
- 1h: commodity avg `0.0217` n `12`; crypto_alt avg `0.87` n `230`; crypto_major avg `1.1938` n `8`; equity avg `-0.0611` n `121`; fx avg `0.0092` n `6`; index avg `0.0024` n `25`; metal avg `-0.0328` n `20`; unknown avg `-0.4024` n `794`
- 4h: commodity avg `0.0559` n `12`; crypto_alt avg `3.8691` n `230`; crypto_major avg `4.2553` n `8`; equity avg `-0.0231` n `121`; fx avg `0.0282` n `6`; index avg `-0.011` n `25`; metal avg `-0.0479` n `20`; unknown avg `-0.0773` n `793`
- 24h: commodity avg `0.1992` n `12`; crypto_alt avg `12.6304` n `230`; crypto_major avg `10.8617` n `8`; equity avg `0.1654` n `121`; fx avg `0.0625` n `6`; index avg `-0.023` n `25`; metal avg `0.1867` n `20`; unknown avg `1.5927` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
