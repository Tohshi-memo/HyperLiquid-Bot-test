# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T09:07:25.527055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `0.1668` n `228`; crypto_major avg `0.2125` n `8`; equity avg `0.2893` n `74`; fx avg `0.0217` n `6`; index avg `-0.0538` n `23`; metal avg `-0.0195` n `18`; unknown avg `0.1417` n `517`
- 1h: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.4126` n `228`; crypto_major avg `-0.4391` n `8`; equity avg `0.0284` n `74`; fx avg `-0.0179` n `6`; index avg `-0.0193` n `23`; metal avg `-0.0154` n `18`; unknown avg `-0.0515` n `517`
- 4h: commodity avg `-0.1563` n `12`; crypto_alt avg `0.7118` n `228`; crypto_major avg `0.581` n `8`; equity avg `0.4199` n `74`; fx avg `-0.265` n `6`; index avg `0.1513` n `23`; metal avg `-0.2439` n `18`; unknown avg `-0.1499` n `507`
- 24h: commodity avg `0.7979` n `12`; crypto_alt avg `-1.0578` n `228`; crypto_major avg `0.1243` n `8`; equity avg `0.6895` n `74`; fx avg `-0.3252` n `6`; index avg `0.0789` n `23`; metal avg `-0.9817` n `18`; unknown avg `-4.6841` n `506`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
