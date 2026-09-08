# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T20:07:29.354922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `0.2245` n `233`; crypto_major avg `0.2682` n `8`; equity avg `0.0095` n `134`; fx avg `0.0037` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0387` n `20`; unknown avg `-0.349` n `795`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `0.0474` n `233`; crypto_major avg `-0.1411` n `8`; equity avg `-0.4586` n `134`; fx avg `0.0137` n `6`; index avg `-0.0716` n `26`; metal avg `-0.144` n `20`; unknown avg `0.6368` n `795`
- 4h: commodity avg `0.3811` n `12`; crypto_alt avg `-1.0425` n `233`; crypto_major avg `-0.4653` n `8`; equity avg `-0.6951` n `134`; fx avg `-0.0343` n `6`; index avg `-0.1093` n `26`; metal avg `-0.2303` n `20`; unknown avg `-0.4009` n `765`
- 24h: commodity avg `0.0513` n `12`; crypto_alt avg `-0.0819` n `232`; crypto_major avg `-0.0497` n `8`; equity avg `0.2298` n `134`; fx avg `-0.0893` n `6`; index avg `-0.1688` n `26`; metal avg `-0.3223` n `20`; unknown avg `3.2369` n `706`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
