# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T14:37:14.624213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4573` n `12`; crypto_alt avg `0.1415` n `228`; crypto_major avg `0.1211` n `8`; equity avg `0.1569` n `67`; fx avg `0.0038` n `6`; index avg `0.1934` n `23`; metal avg `0.0412` n `18`; unknown avg `-0.0039` n `396`
- 1h: commodity avg `-0.8356` n `12`; crypto_alt avg `0.5446` n `228`; crypto_major avg `0.4578` n `8`; equity avg `0.2568` n `67`; fx avg `0.0027` n `6`; index avg `0.2706` n `23`; metal avg `0.0812` n `18`; unknown avg `0.9567` n `396`
- 4h: commodity avg `-0.8802` n `12`; crypto_alt avg `1.1275` n `228`; crypto_major avg `0.7317` n `8`; equity avg `0.4837` n `67`; fx avg `-0.0004` n `6`; index avg `0.5658` n `23`; metal avg `0.1573` n `18`; unknown avg `1.0683` n `396`
- 24h: commodity avg `-0.5097` n `12`; crypto_alt avg `-4.0728` n `228`; crypto_major avg `-3.0791` n `8`; equity avg `-1.1939` n `67`; fx avg `0.0811` n `6`; index avg `0.055` n `23`; metal avg `0.1888` n `18`; unknown avg `-1.7358` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
