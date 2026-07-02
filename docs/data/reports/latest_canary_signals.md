# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T14:07:32.590003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1261` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0707` n `12`; crypto_alt avg `-0.1374` n `229`; crypto_major avg `-0.1314` n `8`; equity avg `-0.1755` n `88`; fx avg `-0.0089` n `6`; index avg `-0.0446` n `25`; metal avg `-0.1534` n `20`; unknown avg `-0.0929` n `763`
- 1h: commodity avg `0.1019` n `12`; crypto_alt avg `0.4969` n `229`; crypto_major avg `0.8164` n `8`; equity avg `0.7432` n `88`; fx avg `-0.0322` n `6`; index avg `0.1026` n `25`; metal avg `0.2157` n `20`; unknown avg `0.066` n `763`
- 4h: commodity avg `0.0229` n `12`; crypto_alt avg `1.0455` n `229`; crypto_major avg `2.149` n `8`; equity avg `1.8244` n `88`; fx avg `0.0059` n `6`; index avg `0.3146` n `25`; metal avg `0.6959` n `20`; unknown avg `-0.2562` n `763`
- 24h: commodity avg `-0.3654` n `12`; crypto_alt avg `3.1789` n `228`; crypto_major avg `4.3643` n `8`; equity avg `-0.2397` n `88`; fx avg `-0.0601` n `6`; index avg `-0.2159` n `25`; metal avg `0.5688` n `20`; unknown avg `1.875` n `739`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
