# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T14:37:23.362861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.18` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0296` n `12`; crypto_alt avg `0.4486` n `228`; crypto_major avg `0.3936` n `8`; equity avg `0.112` n `74`; fx avg `-0.0063` n `6`; index avg `0.02` n `23`; metal avg `-0.0257` n `18`; unknown avg `0.1943` n `516`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `1.2668` n `228`; crypto_major avg `1.2543` n `8`; equity avg `0.6334` n `74`; fx avg `-0.0189` n `6`; index avg `0.2685` n `23`; metal avg `0.0926` n `18`; unknown avg `0.3324` n `516`
- 4h: commodity avg `0.1707` n `12`; crypto_alt avg `0.3806` n `228`; crypto_major avg `0.2271` n `8`; equity avg `0.6905` n `74`; fx avg `-0.0242` n `6`; index avg `0.3631` n `23`; metal avg `-0.0912` n `18`; unknown avg `0.2241` n `516`
- 24h: commodity avg `0.0867` n `12`; crypto_alt avg `2.4386` n `228`; crypto_major avg `2.4342` n `8`; equity avg `1.8929` n `74`; fx avg `0.022` n `6`; index avg `0.4611` n `23`; metal avg `0.6572` n `18`; unknown avg `-3.8993` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
