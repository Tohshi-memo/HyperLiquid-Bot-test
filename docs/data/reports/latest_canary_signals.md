# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T15:37:30.739132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.014` n `12`; crypto_alt avg `0.0744` n `234`; crypto_major avg `-0.1474` n `8`; equity avg `-0.0171` n `140`; fx avg `-0.0026` n `6`; index avg `-0.0309` n `26`; metal avg `-0.06` n `20`; unknown avg `-0.1764` n `934`
- 1h: commodity avg `0.1236` n `12`; crypto_alt avg `1.1769` n `234`; crypto_major avg `0.8288` n `8`; equity avg `-0.3171` n `140`; fx avg `-0.0008` n `6`; index avg `-0.0745` n `26`; metal avg `-0.0556` n `20`; unknown avg `3.4235` n `932`
- 4h: commodity avg `0.4674` n `12`; crypto_alt avg `0.987` n `234`; crypto_major avg `0.5163` n `8`; equity avg `0.6067` n `140`; fx avg `-0.0156` n `6`; index avg `0.0659` n `26`; metal avg `0.1667` n `20`; unknown avg `5.2175` n `892`
- 24h: commodity avg `0.1774` n `12`; crypto_alt avg `1.3437` n `234`; crypto_major avg `1.2854` n `8`; equity avg `0.6944` n `140`; fx avg `-0.2993` n `6`; index avg `0.1141` n `26`; metal avg `-0.0635` n `20`; unknown avg `3978.0708` n `834`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
