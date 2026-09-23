# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T08:07:32.195035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0213` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0362` n `12`; crypto_alt avg `-0.4693` n `234`; crypto_major avg `-0.3247` n `8`; equity avg `-0.054` n `140`; fx avg `-0.0049` n `6`; index avg `-0.0119` n `26`; metal avg `-0.0099` n `20`; unknown avg `2.7972` n `937`
- 1h: commodity avg `0.1344` n `12`; crypto_alt avg `-0.8395` n `234`; crypto_major avg `-0.5919` n `8`; equity avg `-0.0513` n `140`; fx avg `0.0113` n `6`; index avg `-0.0262` n `26`; metal avg `-0.0718` n `20`; unknown avg `2.3571` n `937`
- 4h: commodity avg `0.1893` n `12`; crypto_alt avg `-0.759` n `234`; crypto_major avg `-1.0263` n `8`; equity avg `-0.0757` n `140`; fx avg `0.1403` n `6`; index avg `-0.005` n `26`; metal avg `-0.2439` n `20`; unknown avg `2.6037` n `921`
- 24h: commodity avg `0.0573` n `12`; crypto_alt avg `2.9834` n `234`; crypto_major avg `1.4152` n `8`; equity avg `1.4852` n `140`; fx avg `-0.0691` n `6`; index avg `0.1801` n `26`; metal avg `0.1251` n `20`; unknown avg `1.7912` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
