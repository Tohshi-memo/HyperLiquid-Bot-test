# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T08:37:28.693797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0638` n `12`; crypto_alt avg `0.0817` n `234`; crypto_major avg `0.0561` n `8`; equity avg `0.1652` n `137`; fx avg `-0.0081` n `6`; index avg `0.0286` n `27`; metal avg `0.001` n `20`; unknown avg `0.177` n `913`
- 1h: commodity avg `0.0372` n `12`; crypto_alt avg `0.1889` n `234`; crypto_major avg `0.1558` n `8`; equity avg `0.1295` n `137`; fx avg `0.0502` n `6`; index avg `-0.0258` n `27`; metal avg `-0.1025` n `20`; unknown avg `0.1947` n `911`
- 4h: commodity avg `-0.1784` n `12`; crypto_alt avg `0.9982` n `234`; crypto_major avg `0.6126` n `8`; equity avg `0.4733` n `137`; fx avg `0.0631` n `6`; index avg `0.0368` n `27`; metal avg `0.1317` n `20`; unknown avg `0.1021` n `891`
- 24h: commodity avg `-0.5449` n `12`; crypto_alt avg `3.8759` n `234`; crypto_major avg `2.2841` n `8`; equity avg `1.5051` n `137`; fx avg `0.0934` n `6`; index avg `0.1088` n `27`; metal avg `0.0221` n `20`; unknown avg `0.6955` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
