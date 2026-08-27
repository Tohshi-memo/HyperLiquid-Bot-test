# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T00:52:22.548614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `-0.1919` n `231`; crypto_major avg `-0.0694` n `8`; equity avg `-0.311` n `124`; fx avg `-0.0193` n `6`; index avg `-0.0576` n `25`; metal avg `-0.0603` n `20`; unknown avg `0.0193` n `795`
- 1h: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.6883` n `231`; crypto_major avg `-0.8002` n `8`; equity avg `-0.9263` n `124`; fx avg `-0.0771` n `6`; index avg `-0.2006` n `25`; metal avg `-0.113` n `20`; unknown avg `-0.106` n `795`
- 4h: commodity avg `0.0114` n `12`; crypto_alt avg `1.7769` n `231`; crypto_major avg `1.4865` n `8`; equity avg `0.3099` n `124`; fx avg `-0.0927` n `6`; index avg `0.0636` n `25`; metal avg `0.1089` n `20`; unknown avg `0.6283` n `795`
- 24h: commodity avg `0.3715` n `12`; crypto_alt avg `1.0365` n `231`; crypto_major avg `0.8735` n `8`; equity avg `1.2535` n `124`; fx avg `-0.1581` n `6`; index avg `0.263` n `25`; metal avg `-0.2324` n `20`; unknown avg `1.0139` n `778`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
