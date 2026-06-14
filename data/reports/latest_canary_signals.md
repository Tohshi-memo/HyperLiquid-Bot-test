# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T20:37:30.097008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1438` n `12`; crypto_alt avg `0.3823` n `228`; crypto_major avg `0.3145` n `8`; equity avg `0.1107` n `74`; fx avg `-0.0179` n `6`; index avg `-0.0007` n `23`; metal avg `0.1416` n `18`; unknown avg `0.2709` n `645`
- 1h: commodity avg `-0.1953` n `12`; crypto_alt avg `0.2478` n `228`; crypto_major avg `0.3033` n `8`; equity avg `0.0516` n `74`; fx avg `0.0133` n `6`; index avg `0.017` n `23`; metal avg `0.1388` n `18`; unknown avg `0.1264` n `645`
- 4h: commodity avg `0.0121` n `12`; crypto_alt avg `0.2117` n `228`; crypto_major avg `0.1759` n `8`; equity avg `-0.0135` n `74`; fx avg `0.0103` n `6`; index avg `-0.0436` n `23`; metal avg `0.0705` n `18`; unknown avg `0.1053` n `645`
- 24h: commodity avg `-0.0695` n `12`; crypto_alt avg `-0.7246` n `228`; crypto_major avg `-0.2155` n `8`; equity avg `0.2923` n `74`; fx avg `-0.0194` n `6`; index avg `0.1155` n `23`; metal avg `0.0559` n `18`; unknown avg `1.0965` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
