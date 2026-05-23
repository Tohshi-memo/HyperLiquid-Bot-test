# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T11:07:21.811523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.13` n `12`; crypto_alt avg `0.0517` n `228`; crypto_major avg `0.0126` n `8`; equity avg `-0.0446` n `67`; fx avg `0.0` n `6`; index avg `0.0204` n `23`; metal avg `-0.016` n `18`; unknown avg `-0.205` n `396`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.1666` n `228`; crypto_major avg `0.1173` n `8`; equity avg `0.066` n `67`; fx avg `0.0112` n `6`; index avg `-0.0386` n `23`; metal avg `-0.038` n `18`; unknown avg `-0.3648` n `396`
- 4h: commodity avg `0.0405` n `12`; crypto_alt avg `-1.2549` n `228`; crypto_major avg `-0.7882` n `8`; equity avg `-0.1241` n `67`; fx avg `-0.0266` n `6`; index avg `-0.1375` n `23`; metal avg `-0.131` n `18`; unknown avg `-0.0703` n `386`
- 24h: commodity avg `-0.2982` n `12`; crypto_alt avg `-5.5119` n `228`; crypto_major avg `-3.8728` n `8`; equity avg `-1.5598` n `67`; fx avg `0.0621` n `6`; index avg `-0.1439` n `23`; metal avg `-0.8156` n `18`; unknown avg `-2.2926` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0437`, n `668`, weak_sample_signal
