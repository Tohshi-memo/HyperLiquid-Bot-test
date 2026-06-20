# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T12:52:25.889730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `-0.1337` n `228`; crypto_major avg `-0.0893` n `8`; equity avg `-0.0092` n `78`; fx avg `0.0` n `6`; index avg `0.0015` n `23`; metal avg `-0.0003` n `18`; unknown avg `1.1921` n `701`
- 1h: commodity avg `-0.0148` n `12`; crypto_alt avg `-0.317` n `228`; crypto_major avg `-0.2891` n `8`; equity avg `-0.0386` n `78`; fx avg `0.0099` n `6`; index avg `0.0034` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.0887` n `573`
- 4h: commodity avg `-0.0852` n `12`; crypto_alt avg `-0.1024` n `228`; crypto_major avg `0.1006` n `8`; equity avg `-0.062` n `78`; fx avg `0.0306` n `6`; index avg `0.0264` n `23`; metal avg `0.0217` n `18`; unknown avg `-0.3017` n `573`
- 24h: commodity avg `0.4154` n `12`; crypto_alt avg `-3.326` n `228`; crypto_major avg `-3.5075` n `8`; equity avg `1.1327` n `78`; fx avg `-0.0677` n `6`; index avg `0.2976` n `23`; metal avg `-4.0924` n `18`; unknown avg `-0.2189` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
