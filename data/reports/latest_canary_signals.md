# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T14:37:26.824793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2035` n `12`; crypto_alt avg `0.0171` n `228`; crypto_major avg `-0.0033` n `8`; equity avg `0.7022` n `74`; fx avg `-0.014` n `6`; index avg `0.1645` n `23`; metal avg `-0.0189` n `18`; unknown avg `-0.1457` n `517`
- 1h: commodity avg `0.4039` n `12`; crypto_alt avg `-0.0583` n `228`; crypto_major avg `0.2131` n `8`; equity avg `0.9633` n `74`; fx avg `-0.0252` n `6`; index avg `0.0147` n `23`; metal avg `-0.8209` n `18`; unknown avg `-0.1332` n `517`
- 4h: commodity avg `-0.5839` n `12`; crypto_alt avg `0.7414` n `228`; crypto_major avg `1.2341` n `8`; equity avg `1.4564` n `74`; fx avg `-0.0104` n `6`; index avg `0.5516` n `23`; metal avg `0.051` n `18`; unknown avg `-1.603` n `517`
- 24h: commodity avg `-0.186` n `12`; crypto_alt avg `1.3289` n `228`; crypto_major avg `2.8243` n `8`; equity avg `2.0543` n `74`; fx avg `-0.2846` n `6`; index avg `0.8396` n `23`; metal avg `-0.4224` n `18`; unknown avg `-3.0239` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
