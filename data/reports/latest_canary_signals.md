# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T15:22:17.287629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1212` n `12`; crypto_alt avg `-0.1594` n `228`; crypto_major avg `-0.184` n `8`; equity avg `-0.0163` n `67`; fx avg `-0.0052` n `6`; index avg `0.0068` n `23`; metal avg `0.1406` n `18`; unknown avg `-0.0205` n `386`
- 1h: commodity avg `-0.2999` n `12`; crypto_alt avg `-0.2227` n `228`; crypto_major avg `-0.1898` n `8`; equity avg `0.2425` n `67`; fx avg `0.0341` n `6`; index avg `0.2262` n `23`; metal avg `0.3996` n `18`; unknown avg `0.1153` n `386`
- 4h: commodity avg `-0.8181` n `12`; crypto_alt avg `-0.5026` n `228`; crypto_major avg `-0.2364` n `8`; equity avg `0.1842` n `67`; fx avg `0.001` n `6`; index avg `0.4324` n `23`; metal avg `-0.3713` n `18`; unknown avg `0.7168` n `386`
- 24h: commodity avg `-2.1098` n `12`; crypto_alt avg `0.7108` n `228`; crypto_major avg `-0.6772` n `8`; equity avg `-0.1113` n `67`; fx avg `0.1358` n `6`; index avg `1.1946` n `23`; metal avg `0.0936` n `18`; unknown avg `0.6105` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0425`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0393`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0383`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0334`, n `668`, weak_sample_signal
