# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T00:07:13.765587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1006` n `12`; crypto_alt avg `0.0237` n `228`; crypto_major avg `-0.1391` n `8`; equity avg `-0.106` n `67`; fx avg `-0.0017` n `6`; index avg `-0.0177` n `23`; metal avg `-0.0113` n `18`; unknown avg `-0.0754` n `386`
- 1h: commodity avg `0.1903` n `12`; crypto_alt avg `-1.1874` n `228`; crypto_major avg `-0.7085` n `8`; equity avg `-0.2841` n `67`; fx avg `-0.0047` n `6`; index avg `-0.035` n `23`; metal avg `-0.0842` n `18`; unknown avg `-0.4654` n `386`
- 4h: commodity avg `0.7528` n `12`; crypto_alt avg `-1.2553` n `228`; crypto_major avg `-0.7533` n `8`; equity avg `-0.5137` n `67`; fx avg `-0.0074` n `6`; index avg `-0.1824` n `23`; metal avg `-0.0487` n `18`; unknown avg `-0.6561` n `386`
- 24h: commodity avg `-0.2461` n `12`; crypto_alt avg `-3.8783` n `228`; crypto_major avg `-2.7775` n `8`; equity avg `-1.7211` n `67`; fx avg `0.1578` n `6`; index avg `0.1368` n `23`; metal avg `-0.9749` n `18`; unknown avg `-1.752` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
