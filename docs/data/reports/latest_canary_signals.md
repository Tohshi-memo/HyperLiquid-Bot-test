# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T03:07:32.442942+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0174` n `12`; crypto_alt avg `-0.1008` n `230`; crypto_major avg `-0.1266` n `8`; equity avg `-0.0738` n `98`; fx avg `0.0067` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0033` n `20`; unknown avg `-0.0487` n `773`
- 1h: commodity avg `0.0507` n `12`; crypto_alt avg `-0.1649` n `230`; crypto_major avg `-0.13` n `8`; equity avg `-0.3643` n `98`; fx avg `0.0156` n `6`; index avg `-0.0889` n `25`; metal avg `0.0523` n `20`; unknown avg `-0.0619` n `773`
- 4h: commodity avg `0.1323` n `12`; crypto_alt avg `-0.4128` n `230`; crypto_major avg `-0.4199` n `8`; equity avg `-0.0459` n `98`; fx avg `-0.0549` n `6`; index avg `0.0512` n `25`; metal avg `0.1993` n `20`; unknown avg `-0.0164` n `773`
- 24h: commodity avg `0.7375` n `12`; crypto_alt avg `-0.9095` n `230`; crypto_major avg `-0.8809` n `8`; equity avg `-0.8259` n `98`; fx avg `-0.15` n `6`; index avg `-0.1541` n `25`; metal avg `-0.1751` n `20`; unknown avg `1.7113` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0944`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
