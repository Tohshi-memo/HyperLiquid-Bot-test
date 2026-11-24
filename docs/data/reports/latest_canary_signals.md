# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T16:52:26.686005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4084` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1247` n `13`; crypto_alt avg `0.221` n `239`; crypto_major avg `0.3764` n `8`; equity avg `0.6133` n `168`; fx avg `-0.005` n `6`; index avg `0.071` n `27`; metal avg `0.0568` n `20`; unknown avg `0.381` n `1265`
- 1h: commodity avg `0.3519` n `13`; crypto_alt avg `-0.1305` n `239`; crypto_major avg `-0.2537` n `8`; equity avg `0.0335` n `168`; fx avg `0.0161` n `6`; index avg `0.0233` n `27`; metal avg `-0.1008` n `20`; unknown avg `1.6956` n `1255`
- 4h: commodity avg `0.3506` n `13`; crypto_alt avg `-1.4086` n `239`; crypto_major avg `-1.5338` n `8`; equity avg `-2.1339` n `168`; fx avg `0.047` n `6`; index avg `-0.1254` n `27`; metal avg `-0.7528` n `20`; unknown avg `321.2883` n `1243`
- 24h: commodity avg `0.5387` n `13`; crypto_alt avg `-4.9394` n `239`; crypto_major avg `-4.8447` n `8`; equity avg `-4.5873` n `167`; fx avg `0.2436` n `6`; index avg `-0.3281` n `27`; metal avg `-1.2382` n `20`; unknown avg `175.206` n `1137`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
