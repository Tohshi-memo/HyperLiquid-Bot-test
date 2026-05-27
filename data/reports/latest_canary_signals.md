# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T08:37:22.527393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2106` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0092` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1657` n `12`; crypto_alt avg `0.0302` n `228`; crypto_major avg `0.0745` n `8`; equity avg `0.0728` n `67`; fx avg `-0.0041` n `6`; index avg `-0.0171` n `23`; metal avg `0.0106` n `18`; unknown avg `-0.1068` n `418`
- 1h: commodity avg `-0.4991` n `12`; crypto_alt avg `0.3524` n `228`; crypto_major avg `0.1704` n `8`; equity avg `0.3428` n `67`; fx avg `-0.016` n `6`; index avg `0.1518` n `23`; metal avg `0.215` n `18`; unknown avg `0.0054` n `418`
- 4h: commodity avg `-0.8457` n `12`; crypto_alt avg `1.6193` n `228`; crypto_major avg `1.3649` n `8`; equity avg `0.6411` n `67`; fx avg `0.0284` n `6`; index avg `0.1163` n `23`; metal avg `-0.6443` n `18`; unknown avg `0.4892` n `400`
- 24h: commodity avg `-1.8427` n `12`; crypto_alt avg `-0.3229` n `228`; crypto_major avg `0.3625` n `8`; equity avg `1.0713` n `67`; fx avg `-0.0364` n `6`; index avg `0.97` n `23`; metal avg `-0.516` n `18`; unknown avg `0.5816` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
