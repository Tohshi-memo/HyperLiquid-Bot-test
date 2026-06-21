# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T21:22:29.862992+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.3285` n `228`; crypto_major avg `0.3956` n `8`; equity avg `0.0909` n `78`; fx avg `0.0161` n `6`; index avg `-0.0023` n `23`; metal avg `0.0055` n `18`; unknown avg `0.1013` n `702`
- 1h: commodity avg `-0.0885` n `12`; crypto_alt avg `-1.0402` n `228`; crypto_major avg `-0.7573` n `8`; equity avg `-0.162` n `78`; fx avg `-0.0473` n `6`; index avg `-0.0171` n `23`; metal avg `-0.0475` n `18`; unknown avg `0.2693` n `702`
- 4h: commodity avg `-0.0315` n `12`; crypto_alt avg `-1.3609` n `228`; crypto_major avg `-0.8265` n `8`; equity avg `-0.1967` n `78`; fx avg `-0.0874` n `6`; index avg `-0.0074` n `23`; metal avg `-0.1238` n `18`; unknown avg `0.8243` n `694`
- 24h: commodity avg `0.1327` n `12`; crypto_alt avg `0.152` n `228`; crypto_major avg `-0.7022` n `8`; equity avg `0.0775` n `78`; fx avg `-0.157` n `6`; index avg `0.0141` n `23`; metal avg `-0.15` n `18`; unknown avg `0.7962` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
