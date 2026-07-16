# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T04:52:30.470708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `12`; crypto_alt avg `0.0396` n `230`; crypto_major avg `-0.024` n `8`; equity avg `0.0467` n `94`; fx avg `-0.0079` n `6`; index avg `0.0018` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.1491` n `768`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.0524` n `8`; equity avg `-0.1204` n `94`; fx avg `-0.0113` n `6`; index avg `-0.0402` n `25`; metal avg `-0.0072` n `20`; unknown avg `0.3052` n `768`
- 4h: commodity avg `-0.1061` n `12`; crypto_alt avg `0.0542` n `230`; crypto_major avg `-0.0329` n `8`; equity avg `-0.0229` n `94`; fx avg `-0.0358` n `6`; index avg `-0.0258` n `25`; metal avg `-0.1081` n `20`; unknown avg `-0.5863` n `768`
- 24h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.1621` n `230`; crypto_major avg `-0.0271` n `8`; equity avg `-2.3903` n `93`; fx avg `0.0893` n `6`; index avg `-0.5001` n `25`; metal avg `0.0393` n `20`; unknown avg `-0.1911` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
