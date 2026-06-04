# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T10:52:25.318226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.6932` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.6847` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.9068` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.8806` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.118` n `12`; crypto_alt avg `-0.7175` n `228`; crypto_major avg `-1.0345` n `8`; equity avg `-0.3237` n `73`; fx avg `-0.0012` n `6`; index avg `-0.0808` n `23`; metal avg `-0.0749` n `18`; unknown avg `0.8327` n `424`
- 1h: commodity avg `0.4904` n `12`; crypto_alt avg `-0.4821` n `228`; crypto_major avg `-1.1225` n `8`; equity avg `-0.5708` n `73`; fx avg `-0.0101` n `6`; index avg `-0.2019` n `23`; metal avg `-0.1938` n `18`; unknown avg `0.057` n `424`
- 4h: commodity avg `0.1782` n `12`; crypto_alt avg `-3.8167` n `228`; crypto_major avg `-3.5065` n `8`; equity avg `-1.6259` n `73`; fx avg `0.1126` n `6`; index avg `-0.5997` n `23`; metal avg `0.1867` n `18`; unknown avg `0.0165` n `424`
- 24h: commodity avg `-0.7145` n `12`; crypto_alt avg `-8.3834` n `228`; crypto_major avg `-7.4736` n `8`; equity avg `-4.9772` n `73`; fx avg `0.0508` n `6`; index avg `-1.6234` n `23`; metal avg `-1.0258` n `18`; unknown avg `-0.3651` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
