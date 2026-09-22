# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T19:22:36.352620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `0.2059` n `234`; crypto_major avg `0.0951` n `8`; equity avg `0.023` n `140`; fx avg `0.0051` n `6`; index avg `0.008` n `26`; metal avg `0.0024` n `20`; unknown avg `17.2872` n `942`
- 1h: commodity avg `0.0943` n `12`; crypto_alt avg `0.134` n `234`; crypto_major avg `0.2878` n `8`; equity avg `-0.0206` n `140`; fx avg `0.0105` n `6`; index avg `-0.0149` n `26`; metal avg `0.0373` n `20`; unknown avg `28.5244` n `940`
- 4h: commodity avg `0.014` n `12`; crypto_alt avg `1.1463` n `234`; crypto_major avg `0.5414` n `8`; equity avg `0.4607` n `140`; fx avg `0.0245` n `6`; index avg `0.0634` n `26`; metal avg `0.2632` n `20`; unknown avg `23.5757` n `880`
- 24h: commodity avg `0.129` n `12`; crypto_alt avg `2.6848` n `234`; crypto_major avg `1.3706` n `8`; equity avg `0.776` n `140`; fx avg `-0.2662` n `6`; index avg `0.0842` n `26`; metal avg `0.2652` n `20`; unknown avg `22.3732` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
