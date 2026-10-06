# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T06:52:35.504977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `13`; crypto_alt avg `0.0265` n `235`; crypto_major avg `0.0198` n `8`; equity avg `0.0142` n `149`; fx avg `-0.0114` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.2213` n `1074`
- 1h: commodity avg `-0.3107` n `13`; crypto_alt avg `-0.0244` n `235`; crypto_major avg `-0.1374` n `8`; equity avg `0.0821` n `149`; fx avg `-0.0029` n `6`; index avg `0.0194` n `26`; metal avg `0.0427` n `20`; unknown avg `4.431` n `1044`
- 4h: commodity avg `-0.2875` n `13`; crypto_alt avg `0.0518` n `235`; crypto_major avg `-0.2812` n `8`; equity avg `0.2132` n `149`; fx avg `-0.0084` n `6`; index avg `0.0539` n `26`; metal avg `-0.0737` n `20`; unknown avg `4.972` n `1036`
- 24h: commodity avg `-0.3346` n `13`; crypto_alt avg `-1.0281` n `235`; crypto_major avg `-0.6932` n `8`; equity avg `0.3053` n `149`; fx avg `0.0311` n `6`; index avg `0.1722` n `26`; metal avg `-0.1032` n `20`; unknown avg `587.3437` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1711`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
