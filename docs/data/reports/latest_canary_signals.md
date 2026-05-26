# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T23:07:20.221484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `0.1934` n `228`; crypto_major avg `0.2196` n `8`; equity avg `-0.0153` n `67`; fx avg `-0.0177` n `6`; index avg `0.0373` n `23`; metal avg `0.0865` n `18`; unknown avg `-0.0048` n `418`
- 1h: commodity avg `0.0884` n `12`; crypto_alt avg `0.2438` n `228`; crypto_major avg `0.2829` n `8`; equity avg `0.0009` n `67`; fx avg `-0.0098` n `6`; index avg `0.0394` n `23`; metal avg `0.092` n `18`; unknown avg `-0.1442` n `418`
- 4h: commodity avg `-0.0245` n `12`; crypto_alt avg `0.106` n `228`; crypto_major avg `-0.0852` n `8`; equity avg `0.1731` n `67`; fx avg `0.0109` n `6`; index avg `0.0855` n `23`; metal avg `0.4256` n `18`; unknown avg `-0.7505` n `418`
- 24h: commodity avg `0.7306` n `12`; crypto_alt avg `-1.3571` n `228`; crypto_major avg `-1.3613` n `8`; equity avg `-0.0991` n `67`; fx avg `-0.1328` n `6`; index avg `0.6074` n `23`; metal avg `-0.8758` n `18`; unknown avg `0.0469` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
