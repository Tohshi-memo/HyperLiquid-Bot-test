# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T02:37:30.145584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0517` n `12`; crypto_alt avg `0.0328` n `228`; crypto_major avg `0.0648` n `8`; equity avg `-0.1085` n `79`; fx avg `0.0123` n `6`; index avg `-0.016` n `23`; metal avg `0.0852` n `18`; unknown avg `-0.1416` n `701`
- 1h: commodity avg `-0.0997` n `12`; crypto_alt avg `0.0224` n `228`; crypto_major avg `0.0898` n `8`; equity avg `0.0943` n `79`; fx avg `0.0351` n `6`; index avg `-0.0615` n `23`; metal avg `-0.1013` n `18`; unknown avg `0.105` n `693`
- 4h: commodity avg `-0.4208` n `12`; crypto_alt avg `1.4189` n `228`; crypto_major avg `1.3948` n `8`; equity avg `-0.0759` n `79`; fx avg `0.1482` n `6`; index avg `0.0961` n `23`; metal avg `0.4829` n `18`; unknown avg `1.0906` n `685`
- 24h: commodity avg `-0.3471` n `12`; crypto_alt avg `0.646` n `228`; crypto_major avg `-0.0267` n `8`; equity avg `-0.3185` n `79`; fx avg `0.0352` n `6`; index avg `0.0071` n `23`; metal avg `0.3145` n `18`; unknown avg `0.3577` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
