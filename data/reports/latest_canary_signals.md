# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T16:52:27.616143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.117` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.5161` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9429` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0542` n `13`; crypto_alt avg `-0.2864` n `239`; crypto_major avg `-0.2161` n `8`; equity avg `0.035` n `166`; fx avg `-0.008` n `6`; index avg `0.001` n `27`; metal avg `-0.0811` n `20`; unknown avg `164.7791` n `1266`
- 1h: commodity avg `0.1785` n `13`; crypto_alt avg `-0.3729` n `239`; crypto_major avg `-1.0028` n `8`; equity avg `-0.4966` n `166`; fx avg `-0.0364` n `6`; index avg `-0.0274` n `27`; metal avg `-0.0644` n `20`; unknown avg `0.3745` n `1258`
- 4h: commodity avg `-0.6139` n `13`; crypto_alt avg `2.3949` n `239`; crypto_major avg `2.5031` n `8`; equity avg `5.0192` n `166`; fx avg `-0.1846` n `6`; index avg `0.6046` n `27`; metal avg `0.5602` n `20`; unknown avg `312.64` n `1254`
- 24h: commodity avg `-1.5027` n `13`; crypto_alt avg `2.7127` n `239`; crypto_major avg `3.0158` n `8`; equity avg `6.2079` n `166`; fx avg `-0.0714` n `6`; index avg `0.5592` n `27`; metal avg `0.7121` n `20`; unknown avg `9.3084` n `1057`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
