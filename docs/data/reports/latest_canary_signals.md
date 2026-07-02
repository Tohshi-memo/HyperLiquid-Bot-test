# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T20:37:31.093455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.83` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.0222` n `229`; crypto_major avg `-0.0623` n `8`; equity avg `-0.0239` n `88`; fx avg `-0.001` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0025` n `20`; unknown avg `-0.0713` n `765`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `0.0183` n `229`; crypto_major avg `-0.1905` n `8`; equity avg `0.4445` n `88`; fx avg `0.0194` n `6`; index avg `0.1061` n `25`; metal avg `0.1215` n `20`; unknown avg `0.5266` n `765`
- 4h: commodity avg `0.134` n `12`; crypto_alt avg `0.1567` n `229`; crypto_major avg `0.1958` n `8`; equity avg `0.4546` n `88`; fx avg `0.0045` n `6`; index avg `0.0892` n `25`; metal avg `0.207` n `20`; unknown avg `0.5959` n `763`
- 24h: commodity avg `0.1096` n `12`; crypto_alt avg `2.2349` n `228`; crypto_major avg `3.086` n `8`; equity avg `-2.0494` n `88`; fx avg `-0.0871` n `6`; index avg `-0.4244` n `25`; metal avg `0.9836` n `20`; unknown avg `2.4273` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
