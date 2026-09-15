# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T17:52:36.633784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0504` n `12`; crypto_alt avg `-0.2028` n `233`; crypto_major avg `-0.1025` n `8`; equity avg `-0.1201` n `137`; fx avg `-0.0044` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0037` n `20`; unknown avg `-0.2548` n `917`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `0.4864` n `233`; crypto_major avg `0.7559` n `8`; equity avg `-0.2013` n `137`; fx avg `0.0006` n `6`; index avg `-0.0173` n `27`; metal avg `0.0115` n `20`; unknown avg `0.0542` n `915`
- 4h: commodity avg `0.3269` n `12`; crypto_alt avg `0.4443` n `233`; crypto_major avg `0.21` n `8`; equity avg `-0.8099` n `137`; fx avg `0.0348` n `6`; index avg `-0.1153` n `27`; metal avg `-0.0455` n `20`; unknown avg `0.7839` n `889`
- 24h: commodity avg `0.614` n `12`; crypto_alt avg `-2.0834` n `233`; crypto_major avg `-2.163` n `8`; equity avg `-1.5763` n `137`; fx avg `0.2188` n `6`; index avg `-0.2033` n `27`; metal avg `0.008` n `20`; unknown avg `0.4919` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
