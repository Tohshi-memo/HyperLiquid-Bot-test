# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T16:47:56.072931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2862` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.1909` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.8284` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0088` n `12`; crypto_alt avg `0.5068` n `230`; crypto_major avg `0.5894` n `8`; equity avg `0.1892` n `121`; fx avg `-0.0105` n `6`; index avg `0.0313` n `25`; metal avg `0.0345` n `20`; unknown avg `-0.1298` n `792`
- 1h: commodity avg `-0.0753` n `12`; crypto_alt avg `0.5217` n `230`; crypto_major avg `1.1039` n `8`; equity avg `0.0732` n `121`; fx avg `0.0128` n `6`; index avg `0.0547` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.0895` n `792`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `1.7618` n `230`; crypto_major avg `3.1651` n `8`; equity avg `-0.0258` n `121`; fx avg `0.0106` n `6`; index avg `0.0936` n `25`; metal avg `0.3367` n `20`; unknown avg `0.2146` n `792`
- 24h: commodity avg `-0.118` n `12`; crypto_alt avg `6.3444` n `230`; crypto_major avg `10.5964` n `8`; equity avg `-0.6445` n `121`; fx avg `0.1929` n `6`; index avg `0.0056` n `25`; metal avg `0.2636` n `20`; unknown avg `2.1953` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.21`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
