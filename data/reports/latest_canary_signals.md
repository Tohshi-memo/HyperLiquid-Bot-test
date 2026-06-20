# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T02:07:32.299311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1444` n `12`; crypto_alt avg `-0.1673` n `228`; crypto_major avg `-0.0968` n `8`; equity avg `-0.0235` n `78`; fx avg `0.0007` n `6`; index avg `0.0078` n `23`; metal avg `0.0088` n `18`; unknown avg `-0.0836` n `687`
- 1h: commodity avg `0.1615` n `12`; crypto_alt avg `-0.1099` n `228`; crypto_major avg `0.1104` n `8`; equity avg `-0.0537` n `78`; fx avg `0.0007` n `6`; index avg `0.0061` n `23`; metal avg `-0.0105` n `18`; unknown avg `-0.6356` n `679`
- 4h: commodity avg `-0.0718` n `12`; crypto_alt avg `0.4132` n `228`; crypto_major avg `0.5092` n `8`; equity avg `0.1903` n `78`; fx avg `0.0519` n `6`; index avg `0.0656` n `23`; metal avg `-0.0144` n `18`; unknown avg `-0.5847` n `671`
- 24h: commodity avg `0.4288` n `12`; crypto_alt avg `-3.5889` n `228`; crypto_major avg `-4.3975` n `8`; equity avg `0.8452` n `78`; fx avg `-0.0845` n `6`; index avg `0.2782` n `23`; metal avg `-4.126` n `18`; unknown avg `-0.6718` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
