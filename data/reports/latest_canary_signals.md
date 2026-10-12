# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T04:22:25.898786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `13`; crypto_alt avg `0.0564` n `235`; crypto_major avg `0.0639` n `8`; equity avg `-0.1067` n `151`; fx avg `-0.0025` n `6`; index avg `-0.0269` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0669` n `1133`
- 1h: commodity avg `0.075` n `13`; crypto_alt avg `-0.0459` n `235`; crypto_major avg `-0.0181` n `8`; equity avg `-0.1464` n `151`; fx avg `0.0102` n `6`; index avg `-0.0288` n `26`; metal avg `-0.0207` n `20`; unknown avg `-0.113` n `1125`
- 4h: commodity avg `-0.0895` n `13`; crypto_alt avg `-0.0532` n `235`; crypto_major avg `0.071` n `8`; equity avg `-1.0271` n `151`; fx avg `-0.0533` n `6`; index avg `-0.0958` n `26`; metal avg `-0.053` n `20`; unknown avg `0.2792` n `1097`
- 24h: commodity avg `-0.4742` n `13`; crypto_alt avg `2.9962` n `235`; crypto_major avg `1.3738` n `8`; equity avg `-0.3498` n `151`; fx avg `-0.0632` n `6`; index avg `-0.0094` n `26`; metal avg `0.1328` n `20`; unknown avg `1.052` n `928`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0541`, n `668`, weak_sample_signal
