# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T08:52:32.910879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.027` n `12`; crypto_alt avg `0.0331` n `234`; crypto_major avg `0.0531` n `8`; equity avg `0.0145` n `137`; fx avg `-0.0048` n `6`; index avg `0.014` n `27`; metal avg `0.0201` n `20`; unknown avg `-0.1549` n `919`
- 1h: commodity avg `0.0663` n `12`; crypto_alt avg `-0.3542` n `234`; crypto_major avg `-0.2799` n `8`; equity avg `-0.1126` n `137`; fx avg `0.0207` n `6`; index avg `-0.0012` n `27`; metal avg `-0.067` n `20`; unknown avg `-0.1408` n `911`
- 4h: commodity avg `-0.0195` n `12`; crypto_alt avg `-0.8961` n `234`; crypto_major avg `-0.605` n `8`; equity avg `0.1618` n `137`; fx avg `-0.0059` n `6`; index avg `0.0468` n `27`; metal avg `-0.0663` n `20`; unknown avg `0.8633` n `881`
- 24h: commodity avg `0.0442` n `12`; crypto_alt avg `-3.372` n `234`; crypto_major avg `-2.9778` n `8`; equity avg `0.1848` n `137`; fx avg `0.0704` n `6`; index avg `0.1705` n `27`; metal avg `0.5464` n `20`; unknown avg `18892.8722` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
