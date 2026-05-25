# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T20:37:17.352134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1671` n `12`; crypto_alt avg `-0.4027` n `228`; crypto_major avg `-0.1881` n `8`; equity avg `-0.009` n `67`; fx avg `-0.0324` n `6`; index avg `-0.0137` n `23`; metal avg `0.0166` n `18`; unknown avg `-0.1693` n `405`
- 1h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.1355` n `228`; crypto_major avg `-0.1631` n `8`; equity avg `0.0713` n `67`; fx avg `-0.0207` n `6`; index avg `0.0852` n `23`; metal avg `0.0395` n `18`; unknown avg `-0.3604` n `405`
- 4h: commodity avg `-0.2206` n `12`; crypto_alt avg `-0.3381` n `228`; crypto_major avg `-0.5421` n `8`; equity avg `0.1269` n `67`; fx avg `-0.0135` n `6`; index avg `0.1786` n `23`; metal avg `0.1064` n `18`; unknown avg `-0.3045` n `405`
- 24h: commodity avg `-1.1977` n `12`; crypto_alt avg `2.1051` n `228`; crypto_major avg `0.3548` n `8`; equity avg `0.8212` n `67`; fx avg `-0.0851` n `6`; index avg `0.615` n `23`; metal avg `1.7431` n `18`; unknown avg `1.1923` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
