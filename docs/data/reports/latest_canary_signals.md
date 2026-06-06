# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T13:37:22.221807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5579` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `-0.2177` n `228`; crypto_major avg `-0.3319` n `8`; equity avg `-0.1846` n `74`; fx avg `0.0008` n `6`; index avg `-0.0345` n `23`; metal avg `-0.0189` n `18`; unknown avg `0.7496` n `515`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `0.6239` n `228`; crypto_major avg `0.2772` n `8`; equity avg `0.1392` n `74`; fx avg `0.0052` n `6`; index avg `0.0883` n `23`; metal avg `0.05` n `18`; unknown avg `0.0257` n `417`
- 4h: commodity avg `0.1661` n `12`; crypto_alt avg `-0.8535` n `228`; crypto_major avg `-1.1489` n `8`; equity avg `0.409` n `74`; fx avg `0.0192` n `6`; index avg `0.2381` n `23`; metal avg `0.007` n `18`; unknown avg `0.9048` n `413`
- 24h: commodity avg `-0.5985` n `12`; crypto_alt avg `-3.707` n `228`; crypto_major avg `-3.8175` n `8`; equity avg `-5.0033` n `74`; fx avg `-0.2407` n `6`; index avg `-2.8547` n `23`; metal avg `-2.8453` n `18`; unknown avg `0.0048` n `402`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
