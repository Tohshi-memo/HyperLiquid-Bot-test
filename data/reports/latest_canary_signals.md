# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T05:37:26.194074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0317` n `12`; crypto_alt avg `0.1252` n `230`; crypto_major avg `0.0507` n `8`; equity avg `0.2426` n `98`; fx avg `-0.0093` n `6`; index avg `0.0328` n `25`; metal avg `0.0501` n `20`; unknown avg `-0.1174` n `773`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `0.0611` n `230`; crypto_major avg `-0.0205` n `8`; equity avg `0.1945` n `98`; fx avg `-0.013` n `6`; index avg `0.0118` n `25`; metal avg `-0.0352` n `20`; unknown avg `-0.369` n `773`
- 4h: commodity avg `0.0417` n `12`; crypto_alt avg `-0.0622` n `230`; crypto_major avg `-0.0817` n `8`; equity avg `-0.172` n `98`; fx avg `-0.0174` n `6`; index avg `-0.0266` n `25`; metal avg `0.0632` n `20`; unknown avg `-0.4107` n `773`
- 24h: commodity avg `0.7262` n `12`; crypto_alt avg `-0.0518` n `230`; crypto_major avg `-0.0236` n `8`; equity avg `0.5915` n `98`; fx avg `-0.1451` n `6`; index avg `0.1428` n `25`; metal avg `-0.0668` n `20`; unknown avg `1.554` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
