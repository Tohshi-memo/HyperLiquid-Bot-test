# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T17:07:19.297524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0642` n `12`; crypto_alt avg `0.0583` n `228`; crypto_major avg `-0.0729` n `8`; equity avg `-0.0968` n `67`; fx avg `-0.0083` n `6`; index avg `0.0299` n `23`; metal avg `0.0056` n `18`; unknown avg `-0.4784` n `396`
- 1h: commodity avg `0.0692` n `12`; crypto_alt avg `0.3429` n `228`; crypto_major avg `0.0324` n `8`; equity avg `-0.0687` n `67`; fx avg `-0.0039` n `6`; index avg `0.012` n `23`; metal avg `0.0029` n `18`; unknown avg `-0.3163` n `396`
- 4h: commodity avg `-0.7595` n `12`; crypto_alt avg `1.7827` n `228`; crypto_major avg `1.2271` n `8`; equity avg `0.6016` n `67`; fx avg `-0.0041` n `6`; index avg `0.2222` n `23`; metal avg `0.2284` n `18`; unknown avg `0.8716` n `396`
- 24h: commodity avg `0.325` n `12`; crypto_alt avg `-2.8681` n `228`; crypto_major avg `-2.0014` n `8`; equity avg `-1.0427` n `67`; fx avg `0.0041` n `6`; index avg `-0.2952` n `23`; metal avg `-0.269` n `18`; unknown avg `-1.7303` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
