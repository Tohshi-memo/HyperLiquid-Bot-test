# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T23:07:23.954134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.28` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `0.0883` n `228`; crypto_major avg `0.2487` n `8`; equity avg `-0.0011` n `67`; fx avg `-0.0214` n `6`; index avg `0.0056` n `23`; metal avg `0.0003` n `18`; unknown avg `0.1795` n `386`
- 1h: commodity avg `0.1998` n `12`; crypto_alt avg `-0.1988` n `228`; crypto_major avg `0.1003` n `8`; equity avg `0.1494` n `67`; fx avg `0.0213` n `6`; index avg `0.03` n `23`; metal avg `0.0757` n `18`; unknown avg `-0.0635` n `386`
- 4h: commodity avg `0.0287` n `12`; crypto_alt avg `0.351` n `228`; crypto_major avg `0.1845` n `8`; equity avg `0.5509` n `67`; fx avg `0.0065` n `6`; index avg `0.2738` n `23`; metal avg `0.349` n `18`; unknown avg `-0.2508` n `386`
- 24h: commodity avg `-0.3257` n `12`; crypto_alt avg `2.4212` n `228`; crypto_major avg `1.8691` n `8`; equity avg `2.1151` n `66`; fx avg `0.0936` n `6`; index avg `0.8252` n `23`; metal avg `0.6244` n `18`; unknown avg `5.7147` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
