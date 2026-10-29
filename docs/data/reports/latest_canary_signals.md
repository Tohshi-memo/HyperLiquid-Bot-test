# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T20:37:34.934521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1416` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.0313` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.8442` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.9163` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.762` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0351` n `13`; crypto_alt avg `-0.9922` n `238`; crypto_major avg `-1.1459` n `8`; equity avg `0.0458` n `156`; fx avg `0.0063` n `6`; index avg `0.039` n `27`; metal avg `0.0225` n `20`; unknown avg `-0.0613` n `1244`
- 1h: commodity avg `0.0417` n `13`; crypto_alt avg `-2.0332` n `238`; crypto_major avg `-1.8613` n `8`; equity avg `-1.126` n `156`; fx avg `0.0084` n `6`; index avg `-0.0993` n `27`; metal avg `0.055` n `20`; unknown avg `2.7669` n `1168`
- 4h: commodity avg `0.1716` n `13`; crypto_alt avg `-3.4928` n `238`; crypto_major avg `-2.97` n `8`; equity avg `-1.8415` n `156`; fx avg `0.0185` n `6`; index avg `-0.1258` n `27`; metal avg `0.0613` n `20`; unknown avg `9.0235` n `1170`
- 24h: commodity avg `-0.2134` n `13`; crypto_alt avg `-3.2481` n `238`; crypto_major avg `-0.9496` n `8`; equity avg `-2.0611` n `155`; fx avg `0.0546` n `6`; index avg `-0.1972` n `27`; metal avg `-0.5206` n `20`; unknown avg `31.8269` n `976`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
