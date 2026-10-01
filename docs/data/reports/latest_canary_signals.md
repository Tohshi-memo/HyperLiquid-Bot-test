# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T04:07:33.172860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0995` n `13`; crypto_alt avg `-0.1123` n `234`; crypto_major avg `-0.0527` n `8`; equity avg `0.1342` n `142`; fx avg `0.0074` n `6`; index avg `0.0368` n `26`; metal avg `0.0143` n `20`; unknown avg `-0.2045` n `966`
- 1h: commodity avg `-0.5335` n `13`; crypto_alt avg `0.4993` n `234`; crypto_major avg `0.2307` n `8`; equity avg `0.2962` n `142`; fx avg `0.0091` n `6`; index avg `0.0536` n `26`; metal avg `0.0543` n `20`; unknown avg `0.1124` n `966`
- 4h: commodity avg `-0.6849` n `13`; crypto_alt avg `0.8409` n `234`; crypto_major avg `0.1027` n `8`; equity avg `0.6665` n `142`; fx avg `0.0436` n `6`; index avg `0.182` n `26`; metal avg `0.155` n `20`; unknown avg `-0.0535` n `942`
- 24h: commodity avg `-0.5676` n `13`; crypto_alt avg `1.5159` n `234`; crypto_major avg `0.9046` n `8`; equity avg `0.6133` n `142`; fx avg `0.2107` n `6`; index avg `0.2054` n `26`; metal avg `0.0` n `20`; unknown avg `774.8715` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
