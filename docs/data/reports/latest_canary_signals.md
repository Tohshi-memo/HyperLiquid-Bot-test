# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T05:22:13.996540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0943` n `12`; crypto_alt avg `0.1752` n `228`; crypto_major avg `-0.0418` n `8`; equity avg `0.0115` n `67`; fx avg `-0.0` n `6`; index avg `-0.0205` n `23`; metal avg `-0.0321` n `18`; unknown avg `0.1583` n `386`
- 1h: commodity avg `0.2652` n `12`; crypto_alt avg `0.0013` n `228`; crypto_major avg `-0.111` n `8`; equity avg `0.043` n `67`; fx avg `0.0214` n `6`; index avg `0.0006` n `23`; metal avg `-0.0383` n `18`; unknown avg `-0.2788` n `386`
- 4h: commodity avg `-0.1045` n `12`; crypto_alt avg `1.0265` n `228`; crypto_major avg `0.3994` n `8`; equity avg `0.3423` n `67`; fx avg `0.0585` n `6`; index avg `0.0976` n `23`; metal avg `0.1278` n `18`; unknown avg `-0.5371` n `386`
- 24h: commodity avg `-0.6527` n `12`; crypto_alt avg `2.0471` n `228`; crypto_major avg `0.4345` n `8`; equity avg `1.2881` n `66`; fx avg `0.1025` n `6`; index avg `0.6026` n `23`; metal avg `0.7361` n `18`; unknown avg `2.8863` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
