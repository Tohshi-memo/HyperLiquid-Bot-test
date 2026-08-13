# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T08:07:38.634768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `12`; crypto_alt avg `0.0008` n `230`; crypto_major avg `0.0412` n `8`; equity avg `-0.1745` n `113`; fx avg `0.0003` n `6`; index avg `-0.0153` n `25`; metal avg `-0.0642` n `20`; unknown avg `-0.0215` n `787`
- 1h: commodity avg `-0.1048` n `12`; crypto_alt avg `-0.1086` n `230`; crypto_major avg `-0.0499` n `8`; equity avg `-0.029` n `113`; fx avg `0.0049` n `6`; index avg `-0.009` n `25`; metal avg `-0.1593` n `20`; unknown avg `-0.0579` n `787`
- 4h: commodity avg `-0.0934` n `12`; crypto_alt avg `0.1011` n `230`; crypto_major avg `0.442` n `8`; equity avg `-0.6545` n `113`; fx avg `0.0658` n `6`; index avg `-0.0973` n `25`; metal avg `-0.3152` n `20`; unknown avg `-0.0206` n `755`
- 24h: commodity avg `-0.2744` n `12`; crypto_alt avg `-0.6099` n `230`; crypto_major avg `0.3118` n `8`; equity avg `1.5389` n `113`; fx avg `0.0178` n `6`; index avg `0.2003` n `25`; metal avg `-0.5855` n `20`; unknown avg `-0.0119` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2492`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
