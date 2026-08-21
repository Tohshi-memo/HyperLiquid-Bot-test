# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T08:52:26.683702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.5369` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.262` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.8319` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.6425` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.4498` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.3874` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `0.8125` n `230`; crypto_major avg `1.0466` n `8`; equity avg `0.1785` n `121`; fx avg `0.0161` n `6`; index avg `0.0109` n `25`; metal avg `-0.0522` n `20`; unknown avg `0.1161` n `793`
- 1h: commodity avg `-0.0618` n `12`; crypto_alt avg `1.7023` n `230`; crypto_major avg `2.5807` n `8`; equity avg `0.1933` n `121`; fx avg `-0.0144` n `6`; index avg `-0.017` n `25`; metal avg `0.1309` n `20`; unknown avg `0.3889` n `793`
- 4h: commodity avg `0.0203` n `12`; crypto_alt avg `3.7145` n `230`; crypto_major avg `3.5572` n `8`; equity avg `0.7253` n `121`; fx avg `-0.0024` n `6`; index avg `0.0408` n `25`; metal avg `0.2952` n `20`; unknown avg `0.4066` n `777`
- 24h: commodity avg `0.0138` n `12`; crypto_alt avg `7.9465` n `230`; crypto_major avg `8.177` n `8`; equity avg `0.7949` n `121`; fx avg `-0.1078` n `6`; index avg `0.0783` n `25`; metal avg `0.9353` n `20`; unknown avg `2.651` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2073`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2008`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
