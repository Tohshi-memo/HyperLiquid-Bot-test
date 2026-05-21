# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T04:37:16.713471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.1394` n `228`; crypto_major avg `-0.1434` n `8`; equity avg `-0.0163` n `66`; fx avg `-0.0033` n `6`; index avg `0.005` n `23`; metal avg `-0.0562` n `18`; unknown avg `0.0534` n `384`
- 1h: commodity avg `0.0116` n `12`; crypto_alt avg `-0.2897` n `228`; crypto_major avg `-0.1607` n `8`; equity avg `0.0969` n `66`; fx avg `0.0171` n `6`; index avg `0.0514` n `23`; metal avg `0.0464` n `18`; unknown avg `-0.2509` n `384`
- 4h: commodity avg `-0.0572` n `12`; crypto_alt avg `0.418` n `228`; crypto_major avg `0.5608` n `8`; equity avg `0.576` n `66`; fx avg `0.0623` n `6`; index avg `0.3766` n `23`; metal avg `-0.2776` n `18`; unknown avg `0.4855` n `384`
- 24h: commodity avg `-2.1139` n `12`; crypto_alt avg `3.6883` n `228`; crypto_major avg `3.8135` n `8`; equity avg `2.4739` n `66`; fx avg `0.0423` n `6`; index avg `1.7905` n `23`; metal avg `1.4555` n `18`; unknown avg `5.0628` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
