# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T01:52:28.161962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.0164` n `230`; crypto_major avg `0.0924` n `8`; equity avg `-0.1758` n `98`; fx avg `-0.0337` n `6`; index avg `-0.0338` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.0471` n `773`
- 1h: commodity avg `0.0502` n `12`; crypto_alt avg `-0.3226` n `230`; crypto_major avg `-0.36` n `8`; equity avg `-0.1453` n `98`; fx avg `-0.0569` n `6`; index avg `-0.0257` n `25`; metal avg `0.03` n `20`; unknown avg `0.1781` n `773`
- 4h: commodity avg `0.1791` n `12`; crypto_alt avg `-0.3735` n `230`; crypto_major avg `-0.1986` n `8`; equity avg `0.2186` n `98`; fx avg `-0.0874` n `6`; index avg `0.1011` n `25`; metal avg `0.0243` n `20`; unknown avg `-0.0756` n `773`
- 24h: commodity avg `0.5924` n `12`; crypto_alt avg `-0.7496` n `230`; crypto_major avg `-0.9387` n `8`; equity avg `-0.8774` n `98`; fx avg `-0.1408` n `6`; index avg `-0.126` n `25`; metal avg `-0.1646` n `20`; unknown avg `1.7396` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.073`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0727`, n `666`, weak_sample_signal
