# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T02:52:25.181364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.1105` n `228`; crypto_major avg `-0.0456` n `8`; equity avg `0.0078` n `78`; fx avg `0.0032` n `6`; index avg `0.0126` n `23`; metal avg `0.0039` n `18`; unknown avg `-0.0688` n `687`
- 1h: commodity avg `0.1384` n `12`; crypto_alt avg `-0.4848` n `228`; crypto_major avg `-0.328` n `8`; equity avg `0.0834` n `78`; fx avg `0.0015` n `6`; index avg `0.0363` n `23`; metal avg `0.0044` n `18`; unknown avg `-0.1938` n `687`
- 4h: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.2806` n `228`; crypto_major avg `-0.1792` n `8`; equity avg `0.138` n `78`; fx avg `0.0128` n `6`; index avg `0.092` n `23`; metal avg `-0.0609` n `18`; unknown avg `-0.7136` n `671`
- 24h: commodity avg `0.4221` n `12`; crypto_alt avg `-3.8823` n `228`; crypto_major avg `-4.6176` n `8`; equity avg `0.9577` n `78`; fx avg `-0.0838` n `6`; index avg `0.308` n `23`; metal avg `-4.1308` n `18`; unknown avg `-0.696` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
