# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T21:07:37.629009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4835` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0928` n `12`; crypto_alt avg `0.2773` n `228`; crypto_major avg `0.2257` n `8`; equity avg `0.0773` n `74`; fx avg `-0.0298` n `6`; index avg `0.0194` n `23`; metal avg `0.0676` n `18`; unknown avg `2.5886` n `556`
- 1h: commodity avg `0.066` n `12`; crypto_alt avg `0.1424` n `228`; crypto_major avg `-0.2345` n `8`; equity avg `-0.0605` n `74`; fx avg `-0.0237` n `6`; index avg `-0.0951` n `23`; metal avg `-0.0614` n `18`; unknown avg `-0.2809` n `556`
- 4h: commodity avg `-1.5488` n `12`; crypto_alt avg `1.837` n `228`; crypto_major avg `1.9347` n `8`; equity avg `2.5586` n `74`; fx avg `0.046` n `6`; index avg `1.4239` n `23`; metal avg `2.9388` n `18`; unknown avg `1.1172` n `556`
- 24h: commodity avg `-2.4116` n `12`; crypto_alt avg `4.8421` n `228`; crypto_major avg `4.2068` n `8`; equity avg `4.0895` n `74`; fx avg `0.0355` n `6`; index avg `2.3319` n `23`; metal avg `3.5202` n `18`; unknown avg `2.2201` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
