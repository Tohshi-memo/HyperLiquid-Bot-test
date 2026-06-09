# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T03:37:26.179622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5605` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4385` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0209` n `12`; crypto_alt avg `-0.2394` n `228`; crypto_major avg `-0.272` n `8`; equity avg `0.128` n `74`; fx avg `0.0012` n `6`; index avg `0.0829` n `23`; metal avg `0.1176` n `18`; unknown avg `-0.1389` n `517`
- 1h: commodity avg `-0.1393` n `12`; crypto_alt avg `0.0178` n `228`; crypto_major avg `0.2131` n `8`; equity avg `0.3662` n `74`; fx avg `0.0144` n `6`; index avg `0.178` n `23`; metal avg `0.0385` n `18`; unknown avg `-0.4075` n `517`
- 4h: commodity avg `-0.2411` n `12`; crypto_alt avg `-1.978` n `228`; crypto_major avg `-1.3794` n `8`; equity avg `0.1811` n `74`; fx avg `-0.0569` n `6`; index avg `0.0591` n `23`; metal avg `-0.0134` n `18`; unknown avg `-0.342` n `517`
- 24h: commodity avg `-1.0572` n `12`; crypto_alt avg `-1.1984` n `228`; crypto_major avg `-0.4016` n `8`; equity avg `1.3625` n `74`; fx avg `-0.2888` n `6`; index avg `0.6402` n `23`; metal avg `0.2106` n `18`; unknown avg `-3.1829` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
