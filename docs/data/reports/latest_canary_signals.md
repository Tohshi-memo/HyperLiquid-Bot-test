# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T03:07:25.484314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.0129` n `230`; crypto_major avg `-0.0567` n `8`; equity avg `-0.1632` n `98`; fx avg `0.0295` n `6`; index avg `-0.024` n `25`; metal avg `0.1179` n `20`; unknown avg `-0.0469` n `771`
- 1h: commodity avg `-0.0774` n `12`; crypto_alt avg `0.0062` n `230`; crypto_major avg `-0.11` n `8`; equity avg `-0.4109` n `98`; fx avg `0.0322` n `6`; index avg `-0.043` n `25`; metal avg `0.0581` n `20`; unknown avg `-0.1856` n `771`
- 4h: commodity avg `0.0963` n `12`; crypto_alt avg `0.2815` n `230`; crypto_major avg `0.2134` n `8`; equity avg `-0.3765` n `98`; fx avg `0.0416` n `6`; index avg `-0.0125` n `25`; metal avg `0.506` n `20`; unknown avg `-0.1576` n `771`
- 24h: commodity avg `0.599` n `12`; crypto_alt avg `0.2995` n `230`; crypto_major avg `-0.08` n `8`; equity avg `3.0421` n `98`; fx avg `0.0801` n `6`; index avg `0.4179` n `25`; metal avg `0.9453` n `20`; unknown avg `0.3152` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0956`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0592`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.052`, n `666`, weak_sample_signal
