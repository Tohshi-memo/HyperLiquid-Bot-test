# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T20:22:19.030231+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.356` n `228`; crypto_major avg `-0.3768` n `8`; equity avg `-0.3899` n `66`; fx avg `-0.0009` n `6`; index avg `-0.1251` n `23`; metal avg `-0.1081` n `18`; unknown avg `-0.0675` n `384`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.3415` n `228`; crypto_major avg `-0.2749` n `8`; equity avg `-0.3474` n `66`; fx avg `-0.0608` n `6`; index avg `-0.1287` n `23`; metal avg `-0.1759` n `18`; unknown avg `-0.1759` n `384`
- 4h: commodity avg `-0.2782` n `12`; crypto_alt avg `0.0939` n `228`; crypto_major avg `0.0811` n `8`; equity avg `-0.1034` n `66`; fx avg `-0.0488` n `6`; index avg `0.0264` n `23`; metal avg `0.1964` n `18`; unknown avg `0.7511` n `384`
- 24h: commodity avg `-2.5555` n `12`; crypto_alt avg `2.393` n `228`; crypto_major avg `1.5938` n `8`; equity avg `1.3139` n `66`; fx avg `-0.1123` n `6`; index avg `1.0819` n `23`; metal avg `1.5437` n `18`; unknown avg `0.8133` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
