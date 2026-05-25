# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T18:22:20.597140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `12`; crypto_alt avg `-0.0825` n `228`; crypto_major avg `-0.0539` n `8`; equity avg `-0.0054` n `67`; fx avg `0.0123` n `6`; index avg `0.0707` n `23`; metal avg `0.0239` n `18`; unknown avg `-0.0215` n `405`
- 1h: commodity avg `0.1302` n `12`; crypto_alt avg `-0.0562` n `228`; crypto_major avg `0.0086` n `8`; equity avg `0.0268` n `67`; fx avg `0.0109` n `6`; index avg `-0.038` n `23`; metal avg `-0.1308` n `18`; unknown avg `0.3796` n `405`
- 4h: commodity avg `-0.4094` n `12`; crypto_alt avg `0.4` n `228`; crypto_major avg `-0.3311` n `8`; equity avg `0.0669` n `67`; fx avg `-0.0043` n `6`; index avg `0.28` n `23`; metal avg `0.3426` n `18`; unknown avg `-0.0398` n `405`
- 24h: commodity avg `-1.1927` n `12`; crypto_alt avg `2.1447` n `228`; crypto_major avg `0.577` n `8`; equity avg `0.8607` n `67`; fx avg `-0.0105` n `6`; index avg `0.6941` n `23`; metal avg `1.5709` n `18`; unknown avg `1.1794` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
