# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T17:30:59.069648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8699` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8626` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0189` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0484` n `12`; crypto_alt avg `0.1416` n `229`; crypto_major avg `0.082` n `8`; equity avg `-0.1544` n `88`; fx avg `-0.0039` n `6`; index avg `-0.0285` n `25`; metal avg `0.0563` n `20`; unknown avg `0.2217` n `766`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `0.081` n `229`; crypto_major avg `0.1936` n `8`; equity avg `-0.3788` n `88`; fx avg `0.0113` n `6`; index avg `-0.065` n `25`; metal avg `0.1507` n `20`; unknown avg `0.0806` n `766`
- 4h: commodity avg `0.0765` n `12`; crypto_alt avg `2.9066` n `229`; crypto_major avg `2.9464` n `8`; equity avg `0.9275` n `88`; fx avg `0.0247` n `6`; index avg `0.0845` n `25`; metal avg `0.0838` n `20`; unknown avg `3.8947` n `765`
- 24h: commodity avg `-0.1017` n `12`; crypto_alt avg `1.3002` n `229`; crypto_major avg `1.0085` n `8`; equity avg `-0.3573` n `88`; fx avg `0.2011` n `6`; index avg `0.0202` n `25`; metal avg `-0.258` n `20`; unknown avg `0.8461` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
