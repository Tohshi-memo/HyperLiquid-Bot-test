# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T02:07:19.276823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.1337` n `228`; crypto_major avg `-0.0928` n `8`; equity avg `0.0177` n `67`; fx avg `0.0002` n `6`; index avg `0.0826` n `23`; metal avg `0.0418` n `18`; unknown avg `-0.054` n `396`
- 1h: commodity avg `-0.1312` n `12`; crypto_alt avg `-0.1371` n `228`; crypto_major avg `-0.0237` n `8`; equity avg `0.145` n `67`; fx avg `-0.0079` n `6`; index avg `0.1253` n `23`; metal avg `0.181` n `18`; unknown avg `-0.3318` n `396`
- 4h: commodity avg `0.223` n `12`; crypto_alt avg `-0.4651` n `228`; crypto_major avg `0.3145` n `8`; equity avg `0.3452` n `67`; fx avg `0.0086` n `6`; index avg `0.2863` n `23`; metal avg `0.4914` n `18`; unknown avg `0.1825` n `396`
- 24h: commodity avg `-2.9101` n `12`; crypto_alt avg `2.1577` n `228`; crypto_major avg `2.5607` n `8`; equity avg `2.2729` n `67`; fx avg `0.0417` n `6`; index avg `1.1735` n `23`; metal avg `1.1961` n `18`; unknown avg `1.5374` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
