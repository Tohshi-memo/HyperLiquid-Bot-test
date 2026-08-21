# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:10:21.072089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.1352` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `4.0883` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.9726` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.0689` n `8`; equity avg `0.0093` n `121`; fx avg `0.0013` n `6`; index avg `0.002` n `25`; metal avg `0.0072` n `20`; unknown avg `-0.1642` n `793`
- 1h: commodity avg `0.0207` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `-0.0267` n `8`; equity avg `0.0055` n `121`; fx avg `-0.0043` n `6`; index avg `0.0093` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.035` n `793`
- 4h: commodity avg `0.0148` n `12`; crypto_alt avg `3.0413` n `230`; crypto_major avg `4.1031` n `8`; equity avg `0.1305` n `121`; fx avg `-0.0065` n `6`; index avg `0.0098` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.0355` n `793`
- 24h: commodity avg `0.1762` n `12`; crypto_alt avg `8.7856` n `230`; crypto_major avg `8.3528` n `8`; equity avg `0.9927` n `121`; fx avg `-0.093` n `6`; index avg `0.1106` n `25`; metal avg `0.4466` n `20`; unknown avg `1.4254` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1712`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
