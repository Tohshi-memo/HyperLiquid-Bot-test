# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T17:37:43.795220+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.7038` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `2.5351` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-1.2507` n `12`; crypto_alt avg `1.7605` n `228`; crypto_major avg `1.7172` n `8`; equity avg `1.5435` n `74`; fx avg `0.1094` n `6`; index avg `0.8114` n `23`; metal avg `1.9313` n `18`; unknown avg `0.8777` n `556`
- 1h: commodity avg `-1.6493` n `12`; crypto_alt avg `0.8197` n `228`; crypto_major avg `1.0545` n `8`; equity avg `0.6305` n `74`; fx avg `0.1014` n `6`; index avg `0.4624` n `23`; metal avg `1.6353` n `18`; unknown avg `-0.1754` n `556`
- 4h: commodity avg `-1.4284` n `12`; crypto_alt avg `1.1799` n `228`; crypto_major avg `1.1067` n `8`; equity avg `1.3901` n `74`; fx avg `0.0017` n `6`; index avg `0.8367` n `23`; metal avg `1.7663` n `18`; unknown avg `0.0078` n `556`
- 24h: commodity avg `-2.3563` n `12`; crypto_alt avg `2.6589` n `228`; crypto_major avg `2.5313` n `8`; equity avg `1.383` n `74`; fx avg `0.0526` n `6`; index avg `0.9643` n `23`; metal avg `1.4948` n `18`; unknown avg `1.8106` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
