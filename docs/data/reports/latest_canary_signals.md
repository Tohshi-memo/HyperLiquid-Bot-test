# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T15:52:41.489531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `12`; crypto_alt avg `0.0985` n `234`; crypto_major avg `0.1318` n `8`; equity avg `-0.0226` n `140`; fx avg `0.0095` n `6`; index avg `-0.0056` n `26`; metal avg `-0.0403` n `20`; unknown avg `2.9138` n `942`
- 1h: commodity avg `0.0544` n `12`; crypto_alt avg `1.003` n `234`; crypto_major avg `0.6373` n `8`; equity avg `-0.0139` n `140`; fx avg `-0.0114` n `6`; index avg `-0.0257` n `26`; metal avg `-0.0233` n `20`; unknown avg `0.6153` n `932`
- 4h: commodity avg `0.5485` n `12`; crypto_alt avg `1.0887` n `234`; crypto_major avg `0.6911` n `8`; equity avg `0.669` n `140`; fx avg `-0.0072` n `6`; index avg `0.0585` n `26`; metal avg `0.0725` n `20`; unknown avg `3.2782` n `892`
- 24h: commodity avg `0.1907` n `12`; crypto_alt avg `0.923` n `234`; crypto_major avg `0.7309` n `8`; equity avg `0.6055` n `140`; fx avg `-0.2887` n `6`; index avg `0.0903` n `26`; metal avg `-0.0706` n `20`; unknown avg `3978.0683` n `834`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
