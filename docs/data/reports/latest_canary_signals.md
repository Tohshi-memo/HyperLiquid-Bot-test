# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T05:22:24.881299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0453` n `12`; crypto_alt avg `-0.3629` n `228`; crypto_major avg `-0.3341` n `8`; equity avg `-0.2472` n `74`; fx avg `0.0032` n `6`; index avg `-0.1767` n `23`; metal avg `0.013` n `18`; unknown avg `0.076` n `547`
- 1h: commodity avg `-0.3328` n `12`; crypto_alt avg `-0.7384` n `228`; crypto_major avg `-0.6348` n `8`; equity avg `-0.3747` n `74`; fx avg `0.0151` n `6`; index avg `-0.3037` n `23`; metal avg `-0.1611` n `18`; unknown avg `-0.5248` n `547`
- 4h: commodity avg `-0.3426` n `12`; crypto_alt avg `-1.4588` n `228`; crypto_major avg `-1.5404` n `8`; equity avg `-1.3785` n `74`; fx avg `0.0981` n `6`; index avg `-0.7734` n `23`; metal avg `-0.8783` n `18`; unknown avg `-0.799` n `547`
- 24h: commodity avg `-0.8637` n `12`; crypto_alt avg `-2.2082` n `228`; crypto_major avg `-4.307` n `8`; equity avg `-4.0244` n `74`; fx avg `0.1769` n `6`; index avg `-1.975` n `23`; metal avg `-3.1741` n `18`; unknown avg `0.4481` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
