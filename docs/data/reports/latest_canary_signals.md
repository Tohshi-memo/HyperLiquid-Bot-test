# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T13:37:31.177911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7056` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.216` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.0523` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0724` n `12`; crypto_alt avg `-0.0178` n `230`; crypto_major avg `-0.1433` n `8`; equity avg `-0.419` n `92`; fx avg `0.0031` n `6`; index avg `0.022` n `25`; metal avg `0.0609` n `20`; unknown avg `0.0268` n `766`
- 1h: commodity avg `-0.095` n `12`; crypto_alt avg `0.7352` n `230`; crypto_major avg `0.9875` n `8`; equity avg `-0.2138` n `92`; fx avg `-0.0149` n `6`; index avg `0.0267` n `25`; metal avg `0.1084` n `20`; unknown avg `-0.2192` n `766`
- 4h: commodity avg `-0.1654` n `12`; crypto_alt avg `1.8558` n `230`; crypto_major avg `2.5402` n `8`; equity avg `0.3242` n `92`; fx avg `-0.0093` n `6`; index avg `0.2626` n `25`; metal avg `0.4879` n `20`; unknown avg `1.0683` n `766`
- 24h: commodity avg `1.2323` n `12`; crypto_alt avg `1.1215` n `230`; crypto_major avg `2.3601` n `8`; equity avg `0.0468` n `92`; fx avg `-0.0151` n `6`; index avg `0.1495` n `25`; metal avg `0.3577` n `20`; unknown avg `-0.0522` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
