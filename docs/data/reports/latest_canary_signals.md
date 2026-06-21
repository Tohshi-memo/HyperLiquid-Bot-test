# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T20:37:25.688086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1014` n `228`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0371` n `78`; fx avg `-0.0058` n `6`; index avg `-0.0119` n `23`; metal avg `-0.0113` n `18`; unknown avg `0.2352` n `702`
- 1h: commodity avg `-0.0801` n `12`; crypto_alt avg `-0.3317` n `228`; crypto_major avg `-0.2646` n `8`; equity avg `-0.0573` n `78`; fx avg `-0.048` n `6`; index avg `-0.0044` n `23`; metal avg `-0.0288` n `18`; unknown avg `0.2404` n `702`
- 4h: commodity avg `0.0876` n `12`; crypto_alt avg `-0.1857` n `228`; crypto_major avg `0.2183` n `8`; equity avg `-0.0448` n `78`; fx avg `-0.1289` n `6`; index avg `-0.0188` n `23`; metal avg `-0.0893` n `18`; unknown avg `0.564` n `694`
- 24h: commodity avg `0.329` n `12`; crypto_alt avg `1.4499` n `228`; crypto_major avg `0.2968` n `8`; equity avg `0.2458` n `78`; fx avg `-0.1181` n `6`; index avg `0.0208` n `23`; metal avg `-0.099` n `18`; unknown avg `0.7149` n `645`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
