# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T16:07:26.699493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0534` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0744` n `12`; crypto_alt avg `-0.1944` n `233`; crypto_major avg `-0.2696` n `8`; equity avg `-0.1427` n `137`; fx avg `0.0305` n `6`; index avg `-0.0276` n `27`; metal avg `-0.0282` n `20`; unknown avg `0.068` n `907`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.069` n `233`; crypto_major avg `-0.0215` n `8`; equity avg `-0.0003` n `137`; fx avg `0.0234` n `6`; index avg `-0.0115` n `27`; metal avg `0.0675` n `20`; unknown avg `0.0168` n `907`
- 4h: commodity avg `0.34` n `12`; crypto_alt avg `-0.804` n `233`; crypto_major avg `-1.2183` n `8`; equity avg `-0.9103` n `137`; fx avg `0.059` n `6`; index avg `-0.1649` n `27`; metal avg `0.0306` n `20`; unknown avg `1.6694` n `873`
- 24h: commodity avg `0.306` n `12`; crypto_alt avg `-1.9831` n `233`; crypto_major avg `-2.1274` n `8`; equity avg `-0.9012` n `137`; fx avg `0.2586` n `6`; index avg `-0.1186` n `27`; metal avg `0.028` n `20`; unknown avg `0.4986` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
