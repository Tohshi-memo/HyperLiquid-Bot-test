# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T18:07:21.475475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8933` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0576` n `12`; crypto_alt avg `0.0196` n `228`; crypto_major avg `-0.0493` n `8`; equity avg `0.1739` n `66`; fx avg `-0.0083` n `6`; index avg `0.0233` n `23`; metal avg `0.3171` n `18`; unknown avg `-0.1529` n `384`
- 1h: commodity avg `0.058` n `12`; crypto_alt avg `0.2974` n `228`; crypto_major avg `0.2408` n `8`; equity avg `0.3952` n `66`; fx avg `-0.0029` n `6`; index avg `0.0541` n `23`; metal avg `0.3288` n `18`; unknown avg `-0.2208` n `384`
- 4h: commodity avg `-1.9285` n `12`; crypto_alt avg `1.7471` n `228`; crypto_major avg `0.9648` n `8`; equity avg `1.2274` n `66`; fx avg `-0.0041` n `6`; index avg `0.5369` n `23`; metal avg `1.3949` n `18`; unknown avg `0.4814` n `384`
- 24h: commodity avg `-2.3653` n `12`; crypto_alt avg `2.4368` n `228`; crypto_major avg `1.7231` n `8`; equity avg `1.0615` n `66`; fx avg `-0.0373` n `6`; index avg `0.6718` n `23`; metal avg `1.4154` n `18`; unknown avg `0.7672` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0449`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0411`, n `668`, weak_sample_signal
