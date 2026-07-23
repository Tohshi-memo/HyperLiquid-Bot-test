# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T13:52:34.243121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1213` n `12`; crypto_alt avg `-0.1307` n `230`; crypto_major avg `-0.1147` n `8`; equity avg `0.1001` n `100`; fx avg `0.0172` n `6`; index avg `-0.0405` n `25`; metal avg `-0.0452` n `20`; unknown avg `-0.0313` n `772`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.251` n `230`; crypto_major avg `-0.3914` n `8`; equity avg `0.3553` n `100`; fx avg `0.0006` n `6`; index avg `0.0154` n `25`; metal avg `-0.0656` n `20`; unknown avg `-0.1101` n `772`
- 4h: commodity avg `0.2402` n `12`; crypto_alt avg `-0.597` n `230`; crypto_major avg `-0.9749` n `8`; equity avg `-0.9395` n `99`; fx avg `-0.0047` n `6`; index avg `-0.2332` n `25`; metal avg `-0.3098` n `20`; unknown avg `0.1447` n `772`
- 24h: commodity avg `0.9524` n `12`; crypto_alt avg `-1.0473` n `230`; crypto_major avg `-1.2483` n `8`; equity avg `-0.9905` n `99`; fx avg `-0.0891` n `6`; index avg `-0.1618` n `25`; metal avg `-0.8559` n `20`; unknown avg `-0.0134` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0657`, n `666`, weak_sample_signal
