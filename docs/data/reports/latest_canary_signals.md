# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T15:37:32.722458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7382` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.374` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0674` n `13`; crypto_alt avg `0.2363` n `238`; crypto_major avg `0.1039` n `8`; equity avg `0.1837` n `156`; fx avg `-0.0271` n `6`; index avg `0.0174` n `27`; metal avg `0.0204` n `20`; unknown avg `0.9033` n `1238`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `0.5276` n `238`; crypto_major avg `0.4632` n `8`; equity avg `0.3092` n `156`; fx avg `0.0316` n `6`; index avg `0.0197` n `27`; metal avg `-0.0661` n `20`; unknown avg `0.2637` n `1230`
- 4h: commodity avg `-0.4167` n `13`; crypto_alt avg `2.1599` n `238`; crypto_major avg `2.3215` n `8`; equity avg `0.9012` n `156`; fx avg `0.0527` n `6`; index avg `0.0129` n `27`; metal avg `-0.0525` n `20`; unknown avg `0.8384` n `1132`
- 24h: commodity avg `-0.8564` n `13`; crypto_alt avg `1.2997` n `238`; crypto_major avg `2.8494` n `8`; equity avg `-0.0344` n `155`; fx avg `0.0106` n `6`; index avg `-0.077` n `27`; metal avg `-0.4464` n `20`; unknown avg `14.0624` n `946`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
