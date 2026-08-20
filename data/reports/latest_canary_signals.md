# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T11:37:26.460169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `3.4905` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.7476` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5126` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `0.4825` n `230`; crypto_major avg `0.6835` n `8`; equity avg `-0.0219` n `121`; fx avg `-0.0011` n `6`; index avg `-0.0235` n `25`; metal avg `0.0099` n `20`; unknown avg `0.2908` n `792`
- 1h: commodity avg `0.135` n `12`; crypto_alt avg `0.4884` n `230`; crypto_major avg `0.6387` n `8`; equity avg `-0.367` n `121`; fx avg `0.012` n `6`; index avg `-0.0916` n `25`; metal avg `-0.0832` n `20`; unknown avg `0.3281` n `792`
- 4h: commodity avg `0.2905` n `12`; crypto_alt avg `2.419` n `230`; crypto_major avg `2.8031` n `8`; equity avg `-0.6874` n `121`; fx avg `0.0611` n `6`; index avg `-0.1372` n `25`; metal avg `0.0555` n `20`; unknown avg `0.6832` n `792`
- 24h: commodity avg `0.2666` n `12`; crypto_alt avg `7.9866` n `230`; crypto_major avg `13.0553` n `8`; equity avg `0.2677` n `120`; fx avg `0.2258` n `6`; index avg `0.0425` n `25`; metal avg `0.8648` n `20`; unknown avg `2.8871` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
