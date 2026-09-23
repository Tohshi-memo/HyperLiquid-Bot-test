# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T00:37:29.976295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.4053` n `234`; crypto_major avg `-0.2091` n `8`; equity avg `-0.0089` n `140`; fx avg `-0.0058` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0248` n `20`; unknown avg `4.5015` n `945`
- 1h: commodity avg `0.0799` n `12`; crypto_alt avg `0.1093` n `234`; crypto_major avg `0.4653` n `8`; equity avg `-0.0407` n `140`; fx avg `-0.0416` n `6`; index avg `-0.0398` n `26`; metal avg `-0.0423` n `20`; unknown avg `-0.0217` n `937`
- 4h: commodity avg `0.0585` n `12`; crypto_alt avg `1.0533` n `234`; crypto_major avg `0.4337` n `8`; equity avg `0.118` n `140`; fx avg `-0.0554` n `6`; index avg `-0.0214` n `26`; metal avg `0.0076` n `20`; unknown avg `0.3266` n `936`
- 24h: commodity avg `0.1082` n `12`; crypto_alt avg `2.5399` n `234`; crypto_major avg `0.7332` n `8`; equity avg `0.4263` n `140`; fx avg `-0.23` n `6`; index avg `0.0161` n `26`; metal avg `0.2033` n `20`; unknown avg `1.0987` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
