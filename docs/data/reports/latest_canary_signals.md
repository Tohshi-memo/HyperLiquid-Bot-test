# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T09:07:28.938114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0466` n `12`; crypto_alt avg `0.2994` n `234`; crypto_major avg `0.2918` n `8`; equity avg `0.1149` n `137`; fx avg `0.0097` n `6`; index avg `0.024` n `27`; metal avg `0.0272` n `20`; unknown avg `0.0358` n `917`
- 1h: commodity avg `0.0411` n `12`; crypto_alt avg `0.2682` n `234`; crypto_major avg `0.3481` n `8`; equity avg `0.175` n `137`; fx avg `0.0229` n `6`; index avg `0.0468` n `27`; metal avg `0.003` n `20`; unknown avg `-0.0365` n `911`
- 4h: commodity avg `0.0108` n `12`; crypto_alt avg `-0.3887` n `234`; crypto_major avg `-0.0968` n `8`; equity avg `0.3334` n `137`; fx avg `0.0049` n `6`; index avg `0.0811` n `27`; metal avg `-0.0533` n `20`; unknown avg `6.096` n `881`
- 24h: commodity avg `0.1264` n `12`; crypto_alt avg `-3.0953` n `234`; crypto_major avg `-2.762` n `8`; equity avg `0.2919` n `137`; fx avg `0.0951` n `6`; index avg `0.1947` n `27`; metal avg `0.5581` n `20`; unknown avg `18892.6476` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
