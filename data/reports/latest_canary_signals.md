# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T15:22:22.589364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.16` - Polymarket crypto volume is unusually high.
- 1h_crypto_equity_divergence: score `-2.9326` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-2.4764` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2083` n `12`; crypto_alt avg `0.7345` n `228`; crypto_major avg `0.5296` n `8`; equity avg `3.9188` n `67`; fx avg `-0.0014` n `6`; index avg `0.1826` n `23`; metal avg `0.3247` n `18`; unknown avg `-0.0839` n `385`
- 1h: commodity avg `0.4687` n `12`; crypto_alt avg `0.8908` n `228`; crypto_major avg `1.1254` n `8`; equity avg `4.058` n `67`; fx avg `0.0057` n `6`; index avg `0.0797` n `23`; metal avg `0.3193` n `18`; unknown avg `0.1425` n `385`
- 4h: commodity avg `0.551` n `12`; crypto_alt avg `0.9362` n `228`; crypto_major avg `1.3328` n `8`; equity avg `3.8092` n `67`; fx avg `-0.0789` n `6`; index avg `-0.0546` n `23`; metal avg `0.1569` n `18`; unknown avg `0.4737` n `385`
- 24h: commodity avg `0.8875` n `12`; crypto_alt avg `1.3487` n `228`; crypto_major avg `2.4423` n `8`; equity avg `0.7069` n `66`; fx avg `0.0304` n `6`; index avg `0.155` n `23`; metal avg `-0.7077` n `18`; unknown avg `7.1074` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0456`, n `668`, weak_sample_signal
