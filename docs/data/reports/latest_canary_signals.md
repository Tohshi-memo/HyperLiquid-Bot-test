# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T06:52:20.861455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.3825` n `228`; crypto_major avg `0.3944` n `8`; equity avg `0.0712` n `67`; fx avg `0.0092` n `6`; index avg `0.0308` n `23`; metal avg `0.0178` n `18`; unknown avg `-0.3123` n `396`
- 1h: commodity avg `-0.0654` n `12`; crypto_alt avg `0.3804` n `228`; crypto_major avg `0.2499` n `8`; equity avg `-0.074` n `67`; fx avg `0.0045` n `6`; index avg `-0.0114` n `23`; metal avg `-0.0257` n `18`; unknown avg `-0.023` n `386`
- 4h: commodity avg `-0.3971` n `12`; crypto_alt avg `-0.175` n `228`; crypto_major avg `0.4558` n `8`; equity avg `0.1159` n `67`; fx avg `0.0106` n `6`; index avg `-0.0681` n `23`; metal avg `0.1022` n `18`; unknown avg `-0.3094` n `386`
- 24h: commodity avg `-3.07` n `12`; crypto_alt avg `2.4541` n `228`; crypto_major avg `3.2578` n `8`; equity avg `2.3585` n `67`; fx avg `0.0435` n `6`; index avg `1.2587` n `23`; metal avg `1.2054` n `18`; unknown avg `1.8978` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
