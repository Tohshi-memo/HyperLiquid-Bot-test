# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T20:22:15.807254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1244` n `12`; crypto_alt avg `0.0279` n `228`; crypto_major avg `-0.0407` n `8`; equity avg `-0.0077` n `67`; fx avg `0.006` n `6`; index avg `0.0259` n `23`; metal avg `-0.0039` n `18`; unknown avg `-0.1076` n `405`
- 1h: commodity avg `-0.0947` n `12`; crypto_alt avg `0.0202` n `228`; crypto_major avg `-0.1149` n `8`; equity avg `0.0805` n `67`; fx avg `0.0186` n `6`; index avg `0.0926` n `23`; metal avg `0.0238` n `18`; unknown avg `-0.2478` n `405`
- 4h: commodity avg `-0.4461` n `12`; crypto_alt avg `0.1971` n `228`; crypto_major avg `-0.3206` n `8`; equity avg `0.1441` n `67`; fx avg `0.0208` n `6`; index avg `0.1626` n `23`; metal avg `0.113` n `18`; unknown avg `-0.4252` n `405`
- 24h: commodity avg `-1.2577` n `12`; crypto_alt avg `2.498` n `228`; crypto_major avg `0.4699` n `8`; equity avg `0.8604` n `67`; fx avg `-0.047` n `6`; index avg `0.6358` n `23`; metal avg `1.6865` n `18`; unknown avg `1.2781` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
