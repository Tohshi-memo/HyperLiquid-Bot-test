# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T12:07:18.502135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2907` n `12`; crypto_alt avg `0.2277` n `228`; crypto_major avg `0.2115` n `8`; equity avg `0.1526` n `66`; fx avg `-0.0045` n `6`; index avg `0.0299` n `23`; metal avg `0.0056` n `18`; unknown avg `0.5996` n `384`
- 1h: commodity avg `0.1445` n `12`; crypto_alt avg `-0.1179` n `228`; crypto_major avg `-0.1053` n `8`; equity avg `0.0298` n `66`; fx avg `0.0077` n `6`; index avg `0.0455` n `23`; metal avg `-0.0924` n `18`; unknown avg `1.8556` n `384`
- 4h: commodity avg `-0.1829` n `12`; crypto_alt avg `-0.1216` n `228`; crypto_major avg `0.3247` n `8`; equity avg `0.2914` n `66`; fx avg `0.024` n `6`; index avg `0.2567` n `23`; metal avg `0.2755` n `18`; unknown avg `0.2805` n `384`
- 24h: commodity avg `-0.2977` n `12`; crypto_alt avg `0.9753` n `228`; crypto_major avg `0.852` n `8`; equity avg `1.7845` n `66`; fx avg `-0.0805` n `6`; index avg `0.3542` n `23`; metal avg `-0.5248` n `18`; unknown avg `1.0312` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
