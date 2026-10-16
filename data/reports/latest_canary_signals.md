# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T13:52:32.762085+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0592` n `13`; crypto_alt avg `-0.0731` n `236`; crypto_major avg `-0.0325` n `8`; equity avg `-0.3541` n `151`; fx avg `0.0063` n `6`; index avg `-0.038` n `26`; metal avg `0.0458` n `20`; unknown avg `-0.0648` n `1116`
- 1h: commodity avg `-0.0489` n `13`; crypto_alt avg `-0.2682` n `236`; crypto_major avg `-0.2963` n `8`; equity avg `-1.1541` n `151`; fx avg `0.0308` n `6`; index avg `-0.147` n `26`; metal avg `0.0681` n `20`; unknown avg `55.8875` n `1114`
- 4h: commodity avg `-0.1468` n `13`; crypto_alt avg `-0.4056` n `236`; crypto_major avg `-0.5331` n `8`; equity avg `-1.7817` n `151`; fx avg `0.0363` n `6`; index avg `-0.1664` n `26`; metal avg `0.0412` n `20`; unknown avg `10.7629` n `1108`
- 24h: commodity avg `-0.0873` n `13`; crypto_alt avg `4.9207` n `236`; crypto_major avg `2.9429` n `8`; equity avg `1.9753` n `151`; fx avg `0.0517` n `6`; index avg `0.2256` n `26`; metal avg `0.3471` n `20`; unknown avg `24.7932` n `930`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0813`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
