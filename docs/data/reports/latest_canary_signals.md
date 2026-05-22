# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T14:37:28.471762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2066` n `12`; crypto_alt avg `0.1291` n `228`; crypto_major avg `0.0843` n `8`; equity avg `0.213` n `67`; fx avg `0.0065` n `6`; index avg `0.1522` n `23`; metal avg `0.0375` n `18`; unknown avg `0.0965` n `386`
- 1h: commodity avg `0.1307` n `12`; crypto_alt avg `-0.8881` n `228`; crypto_major avg `-0.6167` n `8`; equity avg `-0.6839` n `67`; fx avg `-0.0159` n `6`; index avg `-0.098` n `23`; metal avg `-0.6243` n `18`; unknown avg `-0.0124` n `386`
- 4h: commodity avg `-0.7138` n `12`; crypto_alt avg `-0.3134` n `228`; crypto_major avg `-0.0136` n `8`; equity avg `0.2508` n `67`; fx avg `-0.0349` n `6`; index avg `0.3889` n `23`; metal avg `-0.8862` n `18`; unknown avg `0.508` n `386`
- 24h: commodity avg `-1.5012` n `12`; crypto_alt avg `1.5105` n `228`; crypto_major avg `-0.1063` n `8`; equity avg `1.0503` n `67`; fx avg `0.1213` n `6`; index avg `1.1119` n `23`; metal avg `-0.1401` n `18`; unknown avg `0.6435` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0437`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0412`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0391`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0326`, n `668`, weak_sample_signal
