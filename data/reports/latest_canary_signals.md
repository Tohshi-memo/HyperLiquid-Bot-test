# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T05:37:34.972179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `0.1077` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.1094` n `113`; fx avg `-0.015` n `6`; index avg `0.0233` n `25`; metal avg `0.0299` n `20`; unknown avg `-0.0913` n `787`
- 1h: commodity avg `0.0799` n `12`; crypto_alt avg `-0.0832` n `230`; crypto_major avg `-0.0525` n `8`; equity avg `-0.0636` n `113`; fx avg `-0.0309` n `6`; index avg `0.0121` n `25`; metal avg `-0.0216` n `20`; unknown avg `-0.3589` n `787`
- 4h: commodity avg `0.1416` n `12`; crypto_alt avg `-0.3497` n `230`; crypto_major avg `-0.2584` n `8`; equity avg `-0.0398` n `113`; fx avg `-0.0195` n `6`; index avg `0.0356` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.3771` n `787`
- 24h: commodity avg `-0.3196` n `12`; crypto_alt avg `-0.5036` n `230`; crypto_major avg `-0.5125` n `8`; equity avg `0.6344` n `113`; fx avg `-0.0027` n `6`; index avg `0.2296` n `25`; metal avg `-0.5741` n `20`; unknown avg `0.8269` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2391`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1892`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
