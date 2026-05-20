# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T11:37:18.818598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.042` n `12`; crypto_alt avg `-0.0434` n `228`; crypto_major avg `-0.0597` n `8`; equity avg `-0.0026` n `66`; fx avg `0.0475` n `6`; index avg `0.0499` n `23`; metal avg `0.1293` n `18`; unknown avg `0.0222` n `384`
- 1h: commodity avg `0.4609` n `12`; crypto_alt avg `-0.2861` n `228`; crypto_major avg `-0.191` n `8`; equity avg `-0.0309` n `66`; fx avg `0.0691` n `6`; index avg `0.0566` n `23`; metal avg `0.0729` n `18`; unknown avg `-0.1799` n `384`
- 4h: commodity avg `-0.2167` n `12`; crypto_alt avg `-0.1369` n `228`; crypto_major avg `0.2264` n `8`; equity avg `0.4183` n `66`; fx avg `0.0446` n `6`; index avg `0.3314` n `23`; metal avg `0.4642` n `18`; unknown avg `-0.2759` n `384`
- 24h: commodity avg `-0.4502` n `12`; crypto_alt avg `0.8696` n `228`; crypto_major avg `0.667` n `8`; equity avg `1.5163` n `66`; fx avg `-0.0608` n `6`; index avg `0.2461` n `23`; metal avg `-0.5182` n `18`; unknown avg `0.5567` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
