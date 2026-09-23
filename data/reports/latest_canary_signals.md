# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T14:07:46.476576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0698` n `12`; crypto_alt avg `-0.46` n `234`; crypto_major avg `-0.2841` n `8`; equity avg `-0.0561` n `140`; fx avg `0.0081` n `6`; index avg `-0.0219` n `26`; metal avg `0.1227` n `20`; unknown avg `0.2397` n `922`
- 1h: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.3162` n `234`; crypto_major avg `0.1827` n `8`; equity avg `-0.3691` n `140`; fx avg `0.0026` n `6`; index avg `-0.1095` n `26`; metal avg `-0.0969` n `20`; unknown avg `512.1775` n `904`
- 4h: commodity avg `0.1714` n `12`; crypto_alt avg `-1.4882` n `234`; crypto_major avg `-0.7188` n `8`; equity avg `-0.8078` n `140`; fx avg `0.0148` n `6`; index avg `-0.1766` n `26`; metal avg `-0.26` n `20`; unknown avg `516.3493` n `898`
- 24h: commodity avg `0.3901` n `12`; crypto_alt avg `1.3269` n `234`; crypto_major avg `-0.8841` n `8`; equity avg `-0.8733` n `140`; fx avg `0.0352` n `6`; index avg `-0.2415` n `26`; metal avg `-0.4574` n `20`; unknown avg `17.2903` n `830`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.2188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.164`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
