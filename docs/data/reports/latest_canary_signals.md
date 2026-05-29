# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T12:22:20.577974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `0.1599` n `228`; crypto_major avg `0.0174` n `8`; equity avg `0.0044` n `69`; fx avg `0.0012` n `6`; index avg `0.0057` n `23`; metal avg `-0.2403` n `18`; unknown avg `-0.2208` n `417`
- 1h: commodity avg `0.1645` n `12`; crypto_alt avg `-0.6803` n `228`; crypto_major avg `-0.5507` n `8`; equity avg `-0.118` n `69`; fx avg `0.0031` n `6`; index avg `-0.0943` n `23`; metal avg `-0.4245` n `18`; unknown avg `-0.305` n `417`
- 4h: commodity avg `-0.38` n `12`; crypto_alt avg `-0.8362` n `228`; crypto_major avg `-0.7176` n `8`; equity avg `-0.2866` n `69`; fx avg `-0.0116` n `6`; index avg `0.1096` n `23`; metal avg `-0.041` n `18`; unknown avg `-0.4265` n `417`
- 24h: commodity avg `-0.1172` n `12`; crypto_alt avg `1.7104` n `228`; crypto_major avg `2.0616` n `8`; equity avg `3.4193` n `69`; fx avg `0.1087` n `6`; index avg `1.4594` n `23`; metal avg `2.1034` n `18`; unknown avg `1.0552` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
