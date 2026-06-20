# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T13:52:30.817996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `12`; crypto_alt avg `0.0961` n `228`; crypto_major avg `0.0633` n `8`; equity avg `0.0169` n `78`; fx avg `-0.0038` n `6`; index avg `-0.0039` n `23`; metal avg `-0.0157` n `18`; unknown avg `0.1114` n `701`
- 1h: commodity avg `0.2457` n `12`; crypto_alt avg `-0.3175` n `228`; crypto_major avg `-0.433` n `8`; equity avg `-0.1988` n `78`; fx avg `-0.0212` n `6`; index avg `-0.0194` n `23`; metal avg `-0.05` n `18`; unknown avg `-0.2637` n `701`
- 4h: commodity avg `0.1519` n `12`; crypto_alt avg `-0.8741` n `228`; crypto_major avg `-0.68` n `8`; equity avg `-0.2826` n `78`; fx avg `0.0039` n `6`; index avg `-0.0297` n `23`; metal avg `-0.0381` n `18`; unknown avg `-0.2105` n `573`
- 24h: commodity avg `0.6656` n `12`; crypto_alt avg `-3.6288` n `228`; crypto_major avg `-3.924` n `8`; equity avg `0.9277` n `78`; fx avg `-0.0887` n `6`; index avg `0.2778` n `23`; metal avg `-4.1398` n `18`; unknown avg `-0.3445` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
