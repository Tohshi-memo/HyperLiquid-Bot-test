# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T04:22:14.328984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0762` n `12`; crypto_alt avg `0.0302` n `228`; crypto_major avg `-0.0091` n `8`; equity avg `0.0472` n `67`; fx avg `-0.0032` n `6`; index avg `0.0068` n `23`; metal avg `0.0358` n `18`; unknown avg `-0.2115` n `386`
- 1h: commodity avg `-0.1731` n `12`; crypto_alt avg `0.394` n `228`; crypto_major avg `0.1117` n `8`; equity avg `0.2709` n `67`; fx avg `0.0069` n `6`; index avg `0.15` n `23`; metal avg `0.3859` n `18`; unknown avg `-0.2599` n `386`
- 4h: commodity avg `-0.2732` n `12`; crypto_alt avg `0.9661` n `228`; crypto_major avg `0.2894` n `8`; equity avg `0.1777` n `67`; fx avg `0.0764` n `6`; index avg `0.1016` n `23`; metal avg `-0.0428` n `18`; unknown avg `-0.3402` n `386`
- 24h: commodity avg `-1.0354` n `12`; crypto_alt avg `1.8298` n `228`; crypto_major avg `0.3458` n `8`; equity avg `1.4629` n `66`; fx avg `0.0908` n `6`; index avg `0.6698` n `23`; metal avg `0.5706` n `18`; unknown avg `2.4288` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0513`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0414`, n `668`, weak_sample_signal
