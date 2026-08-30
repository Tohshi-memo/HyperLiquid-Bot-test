# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T07:22:29.169082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.0739` n `231`; crypto_major avg `-0.0506` n `8`; equity avg `-0.0272` n `128`; fx avg `-0.0005` n `6`; index avg `0.0037` n `26`; metal avg `0.0021` n `20`; unknown avg `0.0206` n `793`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0688` n `231`; crypto_major avg `0.0169` n `8`; equity avg `0.0064` n `128`; fx avg `-0.0025` n `6`; index avg `0.0039` n `26`; metal avg `0.0083` n `20`; unknown avg `0.0369` n `789`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `0.1436` n `231`; crypto_major avg `0.1248` n `8`; equity avg `0.0472` n `128`; fx avg `0.0079` n `6`; index avg `0.0203` n `26`; metal avg `0.0155` n `20`; unknown avg `0.0299` n `759`
- 24h: commodity avg `-0.011` n `12`; crypto_alt avg `0.7562` n `231`; crypto_major avg `0.9957` n `8`; equity avg `0.2775` n `128`; fx avg `0.0002` n `6`; index avg `0.0648` n `26`; metal avg `0.0989` n `20`; unknown avg `0.7936` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
