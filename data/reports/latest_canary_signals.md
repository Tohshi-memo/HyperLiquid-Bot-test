# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T03:07:25.928863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.0755` n `235`; crypto_major avg `0.0098` n `8`; equity avg `0.0085` n `149`; fx avg `0.0089` n `6`; index avg `0.0006` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.3948` n `1072`
- 1h: commodity avg `0.0042` n `13`; crypto_alt avg `-0.2588` n `235`; crypto_major avg `-0.0371` n `8`; equity avg `-0.0571` n `149`; fx avg `0.007` n `6`; index avg `-0.0137` n `26`; metal avg `0.0084` n `20`; unknown avg `-0.2481` n `1072`
- 4h: commodity avg `0.0478` n `13`; crypto_alt avg `-1.4361` n `235`; crypto_major avg `-0.6522` n `8`; equity avg `-0.2081` n `149`; fx avg `0.0177` n `6`; index avg `-0.0652` n `26`; metal avg `-0.0485` n `20`; unknown avg `0.5319` n `1066`
- 24h: commodity avg `-0.0158` n `13`; crypto_alt avg `-1.3148` n `235`; crypto_major avg `-0.5453` n `8`; equity avg `0.0309` n `149`; fx avg `0.0731` n `6`; index avg `0.0907` n `26`; metal avg `0.0674` n `20`; unknown avg `630.8286` n `793`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
