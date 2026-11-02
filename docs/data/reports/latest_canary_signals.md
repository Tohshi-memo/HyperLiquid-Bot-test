# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T18:52:34.095426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4251` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.035` n `13`; crypto_alt avg `-0.1988` n `239`; crypto_major avg `-0.0961` n `8`; equity avg `-0.3828` n `156`; fx avg `0.0007` n `6`; index avg `-0.0397` n `27`; metal avg `-0.0621` n `20`; unknown avg `3.5716` n `1245`
- 1h: commodity avg `0.0322` n `13`; crypto_alt avg `-0.0945` n `239`; crypto_major avg `-0.0201` n `8`; equity avg `-0.4317` n `156`; fx avg `-0.0196` n `6`; index avg `-0.0275` n `27`; metal avg `-0.0336` n `20`; unknown avg `3.8586` n `1221`
- 4h: commodity avg `-0.355` n `13`; crypto_alt avg `-1.7027` n `239`; crypto_major avg `-1.5245` n `8`; equity avg `-1.2864` n `156`; fx avg `0.0018` n `6`; index avg `-0.0994` n `27`; metal avg `-0.1086` n `20`; unknown avg `18.5231` n `1209`
- 24h: commodity avg `-1.3479` n `13`; crypto_alt avg `-2.846` n `238`; crypto_major avg `-1.6535` n `8`; equity avg `-1.9825` n `156`; fx avg `0.2446` n `6`; index avg `0.1161` n `27`; metal avg `0.2424` n `20`; unknown avg `9.0058` n `1035`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
