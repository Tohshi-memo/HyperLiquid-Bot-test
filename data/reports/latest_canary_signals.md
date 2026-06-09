# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T16:37:24.811528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.8188` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0723` n `12`; crypto_alt avg `0.4981` n `228`; crypto_major avg `0.2935` n `8`; equity avg `0.1627` n `74`; fx avg `-0.0144` n `6`; index avg `-0.01` n `23`; metal avg `0.1364` n `18`; unknown avg `0.1703` n `547`
- 1h: commodity avg `-0.5547` n `12`; crypto_alt avg `0.1433` n `228`; crypto_major avg `-0.0361` n `8`; equity avg `-1.3942` n `74`; fx avg `0.0052` n `6`; index avg `-0.9076` n `23`; metal avg `-0.09` n `18`; unknown avg `-0.1354` n `547`
- 4h: commodity avg `-1.225` n `12`; crypto_alt avg `-1.8063` n `228`; crypto_major avg `-2.2948` n `8`; equity avg `-5.1136` n `74`; fx avg `-0.051` n `6`; index avg `-3.068` n `23`; metal avg `-2.3253` n `18`; unknown avg `0.6023` n `545`
- 24h: commodity avg `-1.4687` n `12`; crypto_alt avg `-3.0812` n `228`; crypto_major avg `-3.5331` n `8`; equity avg `-4.5657` n `74`; fx avg `0.1223` n `6`; index avg `-2.6238` n `23`; metal avg `-1.7549` n `18`; unknown avg `-1.4335` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0413`, n `668`, weak_sample_signal
