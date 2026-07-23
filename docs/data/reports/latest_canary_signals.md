# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T20:22:29.791783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `0.1628` n `230`; crypto_major avg `0.1698` n `8`; equity avg `0.2598` n `100`; fx avg `-0.0006` n `6`; index avg `0.0179` n `25`; metal avg `0.0092` n `20`; unknown avg `0.0797` n `772`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.4157` n `230`; crypto_major avg `0.4382` n `8`; equity avg `0.7468` n `100`; fx avg `0.005` n `6`; index avg `0.1343` n `25`; metal avg `0.0308` n `20`; unknown avg `0.5373` n `772`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.0302` n `230`; crypto_major avg `0.1135` n `8`; equity avg `0.1697` n `100`; fx avg `0.0101` n `6`; index avg `0.0674` n `25`; metal avg `-0.0414` n `20`; unknown avg `-0.2355` n `772`
- 24h: commodity avg `0.868` n `12`; crypto_alt avg `-1.2515` n `230`; crypto_major avg `-1.8044` n `8`; equity avg `-1.0331` n `99`; fx avg `-0.0765` n `6`; index avg `-0.2612` n `25`; metal avg `-0.8079` n `20`; unknown avg `-0.4516` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
