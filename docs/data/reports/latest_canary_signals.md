# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T13:55:57.482734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2667` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.5483` n `12`; crypto_alt avg `-0.5703` n `228`; crypto_major avg `-0.3518` n `8`; equity avg `-0.2875` n `74`; fx avg `-0.0009` n `6`; index avg `-0.3135` n `23`; metal avg `-0.3448` n `18`; unknown avg `0.075` n `643`
- 1h: commodity avg `0.7119` n `12`; crypto_alt avg `-1.1894` n `228`; crypto_major avg `-0.7047` n `8`; equity avg `-0.9317` n `74`; fx avg `0.0175` n `6`; index avg `-0.3742` n `23`; metal avg `-0.2048` n `18`; unknown avg `-0.0516` n `643`
- 4h: commodity avg `1.5014` n `12`; crypto_alt avg `-1.3759` n `228`; crypto_major avg `-0.7653` n `8`; equity avg `-1.5947` n `74`; fx avg `-0.007` n `6`; index avg `-0.5851` n `23`; metal avg `-1.0334` n `18`; unknown avg `1.6718` n `643`
- 24h: commodity avg `-1.0377` n `12`; crypto_alt avg `0.6033` n `228`; crypto_major avg `1.0168` n `8`; equity avg `1.067` n `74`; fx avg `0.0221` n `6`; index avg `0.8979` n `23`; metal avg `2.0233` n `18`; unknown avg `1.4594` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
