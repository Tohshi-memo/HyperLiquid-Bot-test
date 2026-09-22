# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T11:52:31.635497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.0014` n `234`; crypto_major avg `-0.0404` n `8`; equity avg `-0.0837` n `140`; fx avg `0.0011` n `6`; index avg `0.0018` n `26`; metal avg `0.0533` n `20`; unknown avg `7.2012` n `944`
- 1h: commodity avg `0.1276` n `12`; crypto_alt avg `0.1149` n `234`; crypto_major avg `0.0871` n `8`; equity avg `-0.28` n `140`; fx avg `0.0056` n `6`; index avg `-0.0314` n `26`; metal avg `-0.0794` n `20`; unknown avg `4.5774` n `942`
- 4h: commodity avg `-0.5703` n `12`; crypto_alt avg `-0.2569` n `234`; crypto_major avg `0.4771` n `8`; equity avg `0.2925` n `140`; fx avg `-0.139` n `6`; index avg `0.0721` n `26`; metal avg `0.1256` n `20`; unknown avg `4.9119` n `934`
- 24h: commodity avg `-0.5106` n `12`; crypto_alt avg `0.0471` n `234`; crypto_major avg `1.2206` n `8`; equity avg `0.8168` n `140`; fx avg `-0.2856` n `6`; index avg `0.2387` n `26`; metal avg `-0.2992` n `20`; unknown avg `1112.5966` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
