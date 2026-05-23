# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T04:52:17.390867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1788` n `12`; crypto_alt avg `-0.1032` n `228`; crypto_major avg `-0.1581` n `8`; equity avg `-0.0732` n `67`; fx avg `0.0` n `6`; index avg `-0.0407` n `23`; metal avg `-0.0317` n `18`; unknown avg `-0.505` n `386`
- 1h: commodity avg `-0.1273` n `12`; crypto_alt avg `-0.5147` n `228`; crypto_major avg `-0.442` n `8`; equity avg `-0.0605` n `67`; fx avg `-0.0012` n `6`; index avg `-0.0338` n `23`; metal avg `-0.0296` n `18`; unknown avg `-0.6537` n `386`
- 4h: commodity avg `-0.0824` n `12`; crypto_alt avg `0.5277` n `228`; crypto_major avg `0.1117` n `8`; equity avg `0.0992` n `67`; fx avg `-0.004` n `6`; index avg `0.1005` n `23`; metal avg `0.0208` n `18`; unknown avg `-1.1458` n `386`
- 24h: commodity avg `0.0213` n `12`; crypto_alt avg `-3.8247` n `228`; crypto_major avg `-2.7282` n `8`; equity avg `-1.9895` n `67`; fx avg `0.0387` n `6`; index avg `-0.1086` n `23`; metal avg `-0.9616` n `18`; unknown avg `-2.0125` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
