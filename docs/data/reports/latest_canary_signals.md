# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T23:45:09.448260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0391` n `12`; crypto_alt avg `-0.0039` n `228`; crypto_major avg `-0.0615` n `8`; equity avg `-0.0282` n `67`; fx avg `-0.0052` n `6`; index avg `0.0115` n `23`; metal avg `-0.0722` n `18`; unknown avg `-0.0427` n `386`
- 1h: commodity avg `-0.179` n `12`; crypto_alt avg `0.051` n `228`; crypto_major avg `0.2356` n `8`; equity avg `-0.0519` n `67`; fx avg `-0.0479` n `6`; index avg `0.0617` n `23`; metal avg `-0.2071` n `18`; unknown avg `0.1294` n `386`
- 4h: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.0968` n `228`; crypto_major avg `-0.082` n `8`; equity avg `0.3625` n `67`; fx avg `-0.0139` n `6`; index avg `0.1893` n `23`; metal avg `-0.1548` n `18`; unknown avg `-0.7052` n `386`
- 24h: commodity avg `-0.6922` n `12`; crypto_alt avg `2.2975` n `228`; crypto_major avg `1.5749` n `8`; equity avg `2.1383` n `66`; fx avg `0.0343` n `6`; index avg `0.8585` n `23`; metal avg `0.318` n `18`; unknown avg `3.7963` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
