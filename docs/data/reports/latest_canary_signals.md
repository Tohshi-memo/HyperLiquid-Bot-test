# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T14:37:24.588798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0568` n `12`; crypto_alt avg `0.1014` n `228`; crypto_major avg `-0.0647` n `8`; equity avg `-0.0551` n `66`; fx avg `-0.0062` n `6`; index avg `-0.029` n `23`; metal avg `0.1473` n `18`; unknown avg `0.0165` n `384`
- 1h: commodity avg `-0.8149` n `12`; crypto_alt avg `1.1851` n `228`; crypto_major avg `0.5927` n `8`; equity avg `0.5323` n `66`; fx avg `-0.0034` n `6`; index avg `0.546` n `23`; metal avg `0.8503` n `18`; unknown avg `0.4042` n `384`
- 4h: commodity avg `-0.5896` n `12`; crypto_alt avg `0.5552` n `228`; crypto_major avg `0.3201` n `8`; equity avg `0.1412` n `66`; fx avg `0.0384` n `6`; index avg `0.572` n `23`; metal avg `0.3097` n `18`; unknown avg `1.7289` n `384`
- 24h: commodity avg `-1.1163` n `12`; crypto_alt avg `2.0192` n `228`; crypto_major avg `1.6007` n `8`; equity avg `2.5539` n `66`; fx avg `-0.0672` n `6`; index avg `1.5644` n `23`; metal avg `1.0607` n `18`; unknown avg `1.9938` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
