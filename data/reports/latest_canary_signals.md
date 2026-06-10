# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T15:07:44.230450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1822` n `12`; crypto_alt avg `0.2366` n `228`; crypto_major avg `0.0743` n `8`; equity avg `-0.5383` n `74`; fx avg `0.0039` n `6`; index avg `-0.2714` n `23`; metal avg `-0.1675` n `18`; unknown avg `-0.0981` n `548`
- 1h: commodity avg `-0.3878` n `12`; crypto_alt avg `-0.3653` n `228`; crypto_major avg `-0.3954` n `8`; equity avg `-0.8528` n `74`; fx avg `-0.0197` n `6`; index avg `-0.4317` n `23`; metal avg `-0.7104` n `18`; unknown avg `-0.161` n `547`
- 4h: commodity avg `0.123` n `12`; crypto_alt avg `1.7768` n `228`; crypto_major avg `1.6813` n `8`; equity avg `1.4658` n `74`; fx avg `-0.0042` n `6`; index avg `0.5251` n `23`; metal avg `0.3621` n `18`; unknown avg `1.4672` n `547`
- 24h: commodity avg `0.9483` n `12`; crypto_alt avg `0.2524` n `228`; crypto_major avg `-0.7425` n `8`; equity avg `-0.9913` n `74`; fx avg `-0.0748` n `6`; index avg `-0.703` n `23`; metal avg `-1.8495` n `18`; unknown avg `1.523` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
