# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T05:52:27.755320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0263` n `12`; crypto_alt avg `-0.0893` n `234`; crypto_major avg `-0.1168` n `8`; equity avg `0.0925` n `137`; fx avg `0.0086` n `6`; index avg `0.0138` n `27`; metal avg `0.0107` n `20`; unknown avg `26.0066` n `919`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.2055` n `234`; crypto_major avg `-0.1215` n `8`; equity avg `0.1177` n `137`; fx avg `0.0357` n `6`; index avg `0.01` n `27`; metal avg `0.0393` n `20`; unknown avg `3.0646` n `917`
- 4h: commodity avg `-0.1017` n `12`; crypto_alt avg `0.6846` n `234`; crypto_major avg `0.5752` n `8`; equity avg `0.8826` n `137`; fx avg `-0.0261` n `6`; index avg `0.1042` n `27`; metal avg `0.3233` n `20`; unknown avg `5.0303` n `907`
- 24h: commodity avg `0.2705` n `12`; crypto_alt avg `-3.3646` n `234`; crypto_major avg `-3.2464` n `8`; equity avg `-0.3344` n `137`; fx avg `0.2089` n `6`; index avg `0.0149` n `27`; metal avg `0.3812` n `20`; unknown avg `18796.1758` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
