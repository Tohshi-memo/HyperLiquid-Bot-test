# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T17:37:27.180163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2828` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0513` n `12`; crypto_alt avg `0.2131` n `228`; crypto_major avg `0.2003` n `8`; equity avg `0.0897` n `69`; fx avg `-0.0077` n `6`; index avg `0.0455` n `23`; metal avg `0.0226` n `18`; unknown avg `0.0935` n `417`
- 1h: commodity avg `-0.1191` n `12`; crypto_alt avg `0.7854` n `228`; crypto_major avg `0.631` n `8`; equity avg `0.1312` n `69`; fx avg `-0.0114` n `6`; index avg `0.0498` n `23`; metal avg `0.0638` n `18`; unknown avg `0.1972` n `417`
- 4h: commodity avg `-0.2287` n `12`; crypto_alt avg `1.6854` n `228`; crypto_major avg `2.0541` n `8`; equity avg `1.9984` n `69`; fx avg `-0.0442` n `6`; index avg `1.2891` n `23`; metal avg `1.9328` n `18`; unknown avg `0.2026` n `417`
- 24h: commodity avg `0.5768` n `12`; crypto_alt avg `-3.4979` n `228`; crypto_major avg `-0.9758` n `8`; equity avg `1.4247` n `68`; fx avg `-0.0205` n `6`; index avg `1.0842` n `23`; metal avg `0.6639` n `18`; unknown avg `-0.7647` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1937`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
