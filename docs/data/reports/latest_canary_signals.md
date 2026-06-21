# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T14:52:25.851401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `0.0207` n `8`; equity avg `0.0087` n `78`; fx avg `-0.0717` n `6`; index avg `-0.0167` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.0051` n `702`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.0432` n `228`; crypto_major avg `0.1381` n `8`; equity avg `-0.0124` n `78`; fx avg `-0.0498` n `6`; index avg `-0.0178` n `23`; metal avg `0.0017` n `18`; unknown avg `-0.0562` n `702`
- 4h: commodity avg `0.1111` n `12`; crypto_alt avg `-0.1838` n `228`; crypto_major avg `-0.3027` n `8`; equity avg `-0.1355` n `78`; fx avg `0.0625` n `6`; index avg `-0.0208` n `23`; metal avg `-0.0905` n `18`; unknown avg `0.081` n `702`
- 24h: commodity avg `0.1289` n `12`; crypto_alt avg `1.4511` n `228`; crypto_major avg `-0.1776` n `8`; equity avg `0.2675` n `78`; fx avg `-0.0247` n `6`; index avg `0.018` n `23`; metal avg `-0.1186` n `18`; unknown avg `0.617` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
