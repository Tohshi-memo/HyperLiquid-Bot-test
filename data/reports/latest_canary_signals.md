# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T06:07:26.036541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `-0.2271` n `228`; crypto_major avg `-0.1293` n `8`; equity avg `0.0138` n `74`; fx avg `-0.0029` n `6`; index avg `0.0357` n `23`; metal avg `-0.0287` n `18`; unknown avg `-0.7869` n `506`
- 1h: commodity avg `-0.035` n `12`; crypto_alt avg `0.3196` n `228`; crypto_major avg `0.2343` n `8`; equity avg `0.1442` n `74`; fx avg `-0.0071` n `6`; index avg `0.0343` n `23`; metal avg `0.0439` n `18`; unknown avg `-0.7386` n `506`
- 4h: commodity avg `-0.0915` n `12`; crypto_alt avg `-0.1889` n `228`; crypto_major avg `0.7742` n `8`; equity avg `0.4406` n `74`; fx avg `-0.0032` n `6`; index avg `0.3342` n `23`; metal avg `0.2637` n `18`; unknown avg `-0.6852` n `506`
- 24h: commodity avg `0.2599` n `12`; crypto_alt avg `2.5543` n `228`; crypto_major avg `1.6666` n `8`; equity avg `1.7478` n `74`; fx avg `0.0446` n `6`; index avg `1.0159` n `23`; metal avg `0.6132` n `18`; unknown avg `1.8722` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
