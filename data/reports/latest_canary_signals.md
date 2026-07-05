# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T14:52:25.362179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.1247` n `229`; crypto_major avg `0.0789` n `8`; equity avg `-0.0239` n `88`; fx avg `0.0005` n `6`; index avg `-0.009` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.1132` n `765`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.043` n `229`; crypto_major avg `0.1428` n `8`; equity avg `-0.0703` n `88`; fx avg `-0.0318` n `6`; index avg `0.0032` n `25`; metal avg `-0.0196` n `20`; unknown avg `0.0867` n `765`
- 4h: commodity avg `-0.028` n `12`; crypto_alt avg `0.4865` n `229`; crypto_major avg `0.7174` n `8`; equity avg `-0.0324` n `88`; fx avg `-0.0685` n `6`; index avg `0.0439` n `25`; metal avg `0.0073` n `20`; unknown avg `0.1959` n `765`
- 24h: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.9252` n `229`; crypto_major avg `-0.5356` n `8`; equity avg `0.2392` n `88`; fx avg `-0.0742` n `6`; index avg `0.0734` n `25`; metal avg `0.0728` n `20`; unknown avg `-1.1206` n `731`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
