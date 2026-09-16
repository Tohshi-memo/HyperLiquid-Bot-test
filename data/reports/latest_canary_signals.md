# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T02:37:27.307144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0454` n `12`; crypto_alt avg `0.2841` n `234`; crypto_major avg `0.3407` n `8`; equity avg `0.2548` n `137`; fx avg `-0.0307` n `6`; index avg `0.0367` n `27`; metal avg `0.1527` n `20`; unknown avg `5.7637` n `919`
- 1h: commodity avg `-0.0862` n `12`; crypto_alt avg `0.3784` n `234`; crypto_major avg `0.6416` n `8`; equity avg `0.2984` n `137`; fx avg `-0.0542` n `6`; index avg `0.0357` n `27`; metal avg `0.1855` n `20`; unknown avg `5.541` n `917`
- 4h: commodity avg `-0.1041` n `12`; crypto_alt avg `0.0769` n `234`; crypto_major avg `0.4849` n `8`; equity avg `0.2122` n `137`; fx avg `0.0673` n `6`; index avg `0.0345` n `27`; metal avg `0.1231` n `20`; unknown avg `-0.3006` n `911`
- 24h: commodity avg `0.2118` n `12`; crypto_alt avg `-3.8065` n `234`; crypto_major avg `-3.583` n `8`; equity avg `-1.3864` n `137`; fx avg `0.2013` n `6`; index avg `-0.1318` n `27`; metal avg `0.2596` n `20`; unknown avg `0.5834` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
