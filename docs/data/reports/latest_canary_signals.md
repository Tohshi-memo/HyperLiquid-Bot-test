# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T08:52:28.422057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0567` n `12`; crypto_alt avg `-0.0175` n `230`; crypto_major avg `-0.0413` n `8`; equity avg `0.0613` n `98`; fx avg `-0.0049` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0465` n `20`; unknown avg `0.0232` n `773`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `0.2791` n `230`; crypto_major avg `0.3198` n `8`; equity avg `0.5202` n `98`; fx avg `-0.0012` n `6`; index avg `0.0582` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.035` n `773`
- 4h: commodity avg `0.1817` n `12`; crypto_alt avg `0.1651` n `230`; crypto_major avg `-0.0285` n `8`; equity avg `0.0838` n `98`; fx avg `0.0283` n `6`; index avg `-0.0548` n `25`; metal avg `-0.3876` n `20`; unknown avg `-0.1325` n `741`
- 24h: commodity avg `0.5892` n `12`; crypto_alt avg `0.0885` n `230`; crypto_major avg `0.0065` n `8`; equity avg `0.7429` n `98`; fx avg `-0.0561` n `6`; index avg `0.1449` n `25`; metal avg `-0.2895` n `20`; unknown avg `11.5272` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.081`, n `666`, weak_sample_signal
