# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T20:22:38.119863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0321` n `12`; crypto_alt avg `0.3196` n `233`; crypto_major avg `0.2348` n `8`; equity avg `0.226` n `135`; fx avg `-0.0109` n `6`; index avg `0.0144` n `26`; metal avg `-0.0188` n `20`; unknown avg `4.2241` n `797`
- 1h: commodity avg `0.0907` n `12`; crypto_alt avg `0.2694` n `233`; crypto_major avg `0.2594` n `8`; equity avg `-0.0762` n `135`; fx avg `-0.002` n `6`; index avg `0.0291` n `26`; metal avg `-0.0372` n `20`; unknown avg `-0.6463` n `775`
- 4h: commodity avg `0.2591` n `12`; crypto_alt avg `1.0612` n `233`; crypto_major avg `0.96` n `8`; equity avg `-0.3778` n `135`; fx avg `0.0003` n `6`; index avg `-0.0134` n `26`; metal avg `-0.2478` n `20`; unknown avg `-0.6685` n `768`
- 24h: commodity avg `1.0628` n `12`; crypto_alt avg `-2.7983` n `233`; crypto_major avg `-2.0594` n `8`; equity avg `-2.047` n `135`; fx avg `0.1071` n `6`; index avg `-0.3118` n `26`; metal avg `-1.2431` n `20`; unknown avg `-1.7571` n `662`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
