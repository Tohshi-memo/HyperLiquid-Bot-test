# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T03:07:27.171340+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.0361` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.6209` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3735` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.3751` n `231`; crypto_major avg `0.4994` n `8`; equity avg `0.1292` n `122`; fx avg `-0.002` n `6`; index avg `0.0306` n `25`; metal avg `0.0502` n `20`; unknown avg `0.9165` n `794`
- 1h: commodity avg `-0.0311` n `12`; crypto_alt avg `1.0429` n `231`; crypto_major avg `1.1724` n `8`; equity avg `0.1113` n `122`; fx avg `0.0057` n `6`; index avg `0.0396` n `25`; metal avg `-0.0707` n `20`; unknown avg `1.5683` n `794`
- 4h: commodity avg `0.0839` n `12`; crypto_alt avg `1.995` n `231`; crypto_major avg `2.7048` n `8`; equity avg `0.3313` n `122`; fx avg `0.0264` n `6`; index avg `0.0204` n `25`; metal avg `-0.3313` n `20`; unknown avg `0.8649` n `794`
- 24h: commodity avg `0.061` n `12`; crypto_alt avg `2.1892` n `231`; crypto_major avg `3.0091` n `8`; equity avg `-1.0292` n `122`; fx avg `0.016` n `6`; index avg `-0.1943` n `25`; metal avg `-0.1263` n `20`; unknown avg `0.6109` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
