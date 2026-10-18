# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T06:37:28.171086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `0.4124` n `237`; crypto_major avg `0.224` n `8`; equity avg `0.1125` n `151`; fx avg `0.0` n `6`; index avg `0.0082` n `26`; metal avg `0.0014` n `20`; unknown avg `0.0316` n `1193`
- 1h: commodity avg `-0.0094` n `13`; crypto_alt avg `0.5975` n `237`; crypto_major avg `0.2801` n `8`; equity avg `0.1543` n `151`; fx avg `-0.0116` n `6`; index avg `0.02` n `26`; metal avg `0.0002` n `20`; unknown avg `0.1852` n `1175`
- 4h: commodity avg `-0.0476` n `13`; crypto_alt avg `-0.1425` n `237`; crypto_major avg `-0.0149` n `8`; equity avg `0.2038` n `151`; fx avg `-0.0109` n `6`; index avg `0.0347` n `26`; metal avg `0.0121` n `20`; unknown avg `0.1484` n `1169`
- 24h: commodity avg `-0.0843` n `13`; crypto_alt avg `-2.5449` n `236`; crypto_major avg `-0.6784` n `8`; equity avg `-0.8536` n `151`; fx avg `-0.0436` n `6`; index avg `-0.1083` n `26`; metal avg `-0.0702` n `20`; unknown avg `3.9447` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1678`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0817`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
