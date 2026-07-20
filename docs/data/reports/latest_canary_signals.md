# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T17:52:30.302662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.1502` n `230`; crypto_major avg `0.2493` n `8`; equity avg `0.1501` n `98`; fx avg `0.006` n `6`; index avg `0.0104` n `25`; metal avg `-0.0484` n `20`; unknown avg `0.008` n `770`
- 1h: commodity avg `0.1011` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.0709` n `8`; equity avg `-0.0209` n `98`; fx avg `0.002` n `6`; index avg `-0.0369` n `25`; metal avg `-0.0368` n `20`; unknown avg `0.2983` n `770`
- 4h: commodity avg `0.1049` n `12`; crypto_alt avg `1.1198` n `230`; crypto_major avg `1.321` n `8`; equity avg `0.1623` n `98`; fx avg `-0.06` n `6`; index avg `-0.0951` n `25`; metal avg `-0.0393` n `20`; unknown avg `0.1613` n `770`
- 24h: commodity avg `-0.4334` n `12`; crypto_alt avg `1.7389` n `230`; crypto_major avg `1.4383` n `8`; equity avg `0.6843` n `98`; fx avg `-0.1511` n `6`; index avg `0.1862` n `25`; metal avg `0.1511` n `20`; unknown avg `0.4406` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0874`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0848`, n `666`, weak_sample_signal
