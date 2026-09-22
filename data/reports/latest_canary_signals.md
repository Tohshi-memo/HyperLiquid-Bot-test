# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T14:52:31.439914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1129` n `12`; crypto_alt avg `0.2687` n `234`; crypto_major avg `0.3223` n `8`; equity avg `-0.3258` n `140`; fx avg `0.0201` n `6`; index avg `-0.0544` n `26`; metal avg `-0.0725` n `20`; unknown avg `3.4566` n `942`
- 1h: commodity avg `0.2613` n `12`; crypto_alt avg `-0.8539` n `234`; crypto_major avg `-0.6931` n `8`; equity avg `-0.2906` n `140`; fx avg `0.0068` n `6`; index avg `-0.0382` n `26`; metal avg `-0.1414` n `20`; unknown avg `1.7128` n `920`
- 4h: commodity avg `0.6228` n `12`; crypto_alt avg `0.1903` n `234`; crypto_major avg `0.1399` n `8`; equity avg `0.398` n `140`; fx avg `0.0099` n `6`; index avg `0.0528` n `26`; metal avg `0.0162` n `20`; unknown avg `1.8246` n `892`
- 24h: commodity avg `0.1448` n `12`; crypto_alt avg `-0.3007` n `234`; crypto_major avg `0.4061` n `8`; equity avg `1.0185` n `140`; fx avg `-0.2755` n `6`; index avg `0.2038` n `26`; metal avg `-0.0458` n `20`; unknown avg `8665.8293` n `842`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
