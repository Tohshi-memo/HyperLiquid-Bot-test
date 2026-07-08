# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T00:07:27.271841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0344` n `12`; crypto_alt avg `0.1477` n `229`; crypto_major avg `0.0394` n `8`; equity avg `0.3196` n `91`; fx avg `-0.0134` n `6`; index avg `0.0528` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.2465` n `763`
- 1h: commodity avg `0.0299` n `12`; crypto_alt avg `-0.0925` n `229`; crypto_major avg `-0.2705` n `8`; equity avg `0.108` n `91`; fx avg `0.0638` n `6`; index avg `0.023` n `25`; metal avg `-0.0668` n `20`; unknown avg `1.474` n `763`
- 4h: commodity avg `0.1624` n `12`; crypto_alt avg `-0.682` n `229`; crypto_major avg `-0.5914` n `8`; equity avg `-0.3541` n `91`; fx avg `0.0687` n `6`; index avg `-0.0564` n `25`; metal avg `-0.2128` n `20`; unknown avg `-0.1014` n `763`
- 24h: commodity avg `0.921` n `12`; crypto_alt avg `-2.6143` n `229`; crypto_major avg `-1.6725` n `8`; equity avg `-3.1085` n `91`; fx avg `-0.1999` n `6`; index avg `-0.5177` n `25`; metal avg `-0.639` n `20`; unknown avg `-0.289` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
