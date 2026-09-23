# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T09:22:26.909519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0587` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.2819` n `234`; crypto_major avg `0.0675` n `8`; equity avg `0.044` n `140`; fx avg `-0.032` n `6`; index avg `0.0037` n `26`; metal avg `0.006` n `20`; unknown avg `0.5194` n `945`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0084` n `234`; crypto_major avg `-0.4962` n `8`; equity avg `-0.094` n `140`; fx avg `-0.0209` n `6`; index avg `-0.0099` n `26`; metal avg `-0.0256` n `20`; unknown avg `1.1494` n `943`
- 4h: commodity avg `0.2024` n `12`; crypto_alt avg `-0.1649` n `234`; crypto_major avg `-1.0683` n `8`; equity avg `-0.0786` n `140`; fx avg `0.1059` n `6`; index avg `-0.0096` n `26`; metal avg `-0.2397` n `20`; unknown avg `0.3088` n `921`
- 24h: commodity avg `0.3489` n `12`; crypto_alt avg `3.8326` n `234`; crypto_major avg `0.9745` n `8`; equity avg `1.2255` n `140`; fx avg `0.0028` n `6`; index avg `0.1285` n `26`; metal avg `0.0155` n `20`; unknown avg `1.4295` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
