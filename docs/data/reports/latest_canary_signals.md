# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T19:22:16.052483+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0357` n `12`; crypto_alt avg `0.0458` n `228`; crypto_major avg `0.0272` n `8`; equity avg `-0.0097` n `67`; fx avg `-0.001` n `6`; index avg `-0.0026` n `23`; metal avg `-0.0151` n `18`; unknown avg `-0.0185` n `405`
- 1h: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.1708` n `228`; crypto_major avg `-0.1836` n `8`; equity avg `-0.0394` n `67`; fx avg `-0.0046` n `6`; index avg `-0.1658` n `23`; metal avg `-0.0132` n `18`; unknown avg `0.0655` n `405`
- 4h: commodity avg `-0.2135` n `12`; crypto_alt avg `0.26` n `228`; crypto_major avg `-0.355` n `8`; equity avg `-0.0502` n `67`; fx avg `-0.0063` n `6`; index avg `0.0795` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.0564` n `405`
- 24h: commodity avg `-1.2481` n `12`; crypto_alt avg `2.1638` n `228`; crypto_major avg `0.3025` n `8`; equity avg `0.8513` n `67`; fx avg `-0.0307` n `6`; index avg `0.5053` n `23`; metal avg `1.621` n `18`; unknown avg `1.3096` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
