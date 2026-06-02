# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T06:52:25.543353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.7` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-2.1382` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7535` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.242` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2738` n `12`; crypto_alt avg `-0.0981` n `228`; crypto_major avg `-0.0473` n `8`; equity avg `0.0044` n `69`; fx avg `0.0339` n `6`; index avg `-0.0366` n `23`; metal avg `-0.0538` n `18`; unknown avg `0.8657` n `422`
- 1h: commodity avg `0.1894` n `12`; crypto_alt avg `-0.0789` n `228`; crypto_major avg `-0.1474` n `8`; equity avg `0.1081` n `69`; fx avg `0.0937` n `6`; index avg `-0.0364` n `23`; metal avg `0.1798` n `18`; unknown avg `-0.2344` n `412`
- 4h: commodity avg `-0.1643` n `12`; crypto_alt avg `-0.3631` n `228`; crypto_major avg `-0.9032` n `8`; equity avg `0.8503` n `69`; fx avg `0.1138` n `6`; index avg `0.3388` n `23`; metal avg `1.235` n `18`; unknown avg `-0.0966` n `412`
- 24h: commodity avg `-0.8548` n `12`; crypto_alt avg `-0.3488` n `228`; crypto_major avg `-1.6231` n `8`; equity avg `0.1894` n `69`; fx avg `0.203` n `6`; index avg `-0.6587` n `23`; metal avg `1.1492` n `18`; unknown avg `2.8427` n `406`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
