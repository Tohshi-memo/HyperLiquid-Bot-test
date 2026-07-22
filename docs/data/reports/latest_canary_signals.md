# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T21:22:26.317351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0593` n `12`; crypto_alt avg `-0.0255` n `230`; crypto_major avg `-0.019` n `8`; equity avg `-0.1452` n `98`; fx avg `-0.0015` n `6`; index avg `-0.0422` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0153` n `773`
- 1h: commodity avg `0.0676` n `12`; crypto_alt avg `0.0896` n `230`; crypto_major avg `-0.0661` n `8`; equity avg `0.0681` n `98`; fx avg `-0.0019` n `6`; index avg `-0.0316` n `25`; metal avg `-0.027` n `20`; unknown avg `0.0645` n `773`
- 4h: commodity avg `0.0406` n `12`; crypto_alt avg `-0.2559` n `230`; crypto_major avg `-0.1506` n `8`; equity avg `-0.1185` n `98`; fx avg `0.005` n `6`; index avg `-0.0548` n `25`; metal avg `-0.0562` n `20`; unknown avg `0.2158` n `773`
- 24h: commodity avg `0.5174` n `12`; crypto_alt avg `-0.4081` n `230`; crypto_major avg `-0.7016` n `8`; equity avg `-0.8621` n `98`; fx avg `-0.0328` n `6`; index avg `-0.1365` n `25`; metal avg `0.2714` n `20`; unknown avg `1.0748` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
