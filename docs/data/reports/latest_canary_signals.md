# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T11:22:27.583771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.6535` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.0145` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6124` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1513` n `12`; crypto_alt avg `-0.0832` n `228`; crypto_major avg `0.0905` n `8`; equity avg `-0.0283` n `73`; fx avg `0.0048` n `6`; index avg `-0.0013` n `23`; metal avg `0.176` n `18`; unknown avg `0.0214` n `424`
- 1h: commodity avg `-0.2962` n `12`; crypto_alt avg `-0.7931` n `228`; crypto_major avg `-0.735` n `8`; equity avg `-0.1664` n `73`; fx avg `0.0078` n `6`; index avg `-0.1006` n `23`; metal avg `0.2186` n `18`; unknown avg `0.5994` n `424`
- 4h: commodity avg `-0.1204` n `12`; crypto_alt avg `-2.5803` n `228`; crypto_major avg `-2.1349` n `8`; equity avg `-1.248` n `73`; fx avg `0.0561` n `6`; index avg `-0.5225` n `23`; metal avg `0.5186` n `18`; unknown avg `-0.7938` n `424`
- 24h: commodity avg `-0.8641` n `12`; crypto_alt avg `-8.9174` n `228`; crypto_major avg `-7.4924` n `8`; equity avg `-5.0333` n `73`; fx avg `0.0616` n `6`; index avg `-1.6304` n `23`; metal avg `-0.7878` n `18`; unknown avg `-1.4961` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
