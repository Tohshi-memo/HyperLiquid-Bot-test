# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T15:07:40.493715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0602` n `12`; crypto_alt avg `0.3503` n `228`; crypto_major avg `0.354` n `8`; equity avg `0.2183` n `74`; fx avg `-0.0404` n `6`; index avg `0.0502` n `23`; metal avg `0.0317` n `18`; unknown avg `0.1565` n `645`
- 1h: commodity avg `-0.0706` n `12`; crypto_alt avg `-0.4816` n `228`; crypto_major avg `-0.4178` n `8`; equity avg `-0.0133` n `74`; fx avg `-0.0443` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.0511` n `645`
- 4h: commodity avg `0.319` n `12`; crypto_alt avg `-0.9276` n `228`; crypto_major avg `-0.711` n `8`; equity avg `-0.2155` n `74`; fx avg `-0.013` n `6`; index avg `0.0568` n `23`; metal avg `-0.0632` n `18`; unknown avg `0.1365` n `645`
- 24h: commodity avg `-0.1123` n `12`; crypto_alt avg `-1.5255` n `228`; crypto_major avg `-0.8601` n `8`; equity avg `0.4453` n `74`; fx avg `-0.0393` n `6`; index avg `0.1203` n `23`; metal avg `-0.1048` n `18`; unknown avg `-1.3362` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
