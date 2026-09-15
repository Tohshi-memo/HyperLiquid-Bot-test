# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T18:07:32.580882+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0799` n `12`; crypto_alt avg `-0.4125` n `233`; crypto_major avg `-0.4204` n `8`; equity avg `0.0505` n `137`; fx avg `-0.0172` n `6`; index avg `0.0206` n `27`; metal avg `0.0331` n `20`; unknown avg `-0.0437` n `915`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `0.5671` n `233`; crypto_major avg `0.8184` n `8`; equity avg `0.0241` n `137`; fx avg `-0.0249` n `6`; index avg `0.0168` n `27`; metal avg `0.0767` n `20`; unknown avg `0.0423` n `915`
- 4h: commodity avg `0.2408` n `12`; crypto_alt avg `-0.1317` n `233`; crypto_major avg `-0.3843` n `8`; equity avg `-0.5877` n `137`; fx avg `0.0234` n `6`; index avg `-0.056` n `27`; metal avg `-0.0054` n `20`; unknown avg `0.2694` n `889`
- 24h: commodity avg `0.5682` n `12`; crypto_alt avg `-2.6382` n `233`; crypto_major avg `-2.7607` n `8`; equity avg `-1.4992` n `137`; fx avg `0.2015` n `6`; index avg `-0.1729` n `27`; metal avg `0.0414` n `20`; unknown avg `0.5538` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
