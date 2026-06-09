# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T10:07:25.638739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1607` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2295` n `12`; crypto_alt avg `-0.0808` n `228`; crypto_major avg `-0.0571` n `8`; equity avg `-0.1066` n `74`; fx avg `0.0201` n `6`; index avg `0.0081` n `23`; metal avg `-0.1221` n `18`; unknown avg `0.0044` n `547`
- 1h: commodity avg `0.18` n `12`; crypto_alt avg `-0.362` n `228`; crypto_major avg `-0.3834` n `8`; equity avg `0.0253` n `74`; fx avg `0.062` n `6`; index avg `0.0486` n `23`; metal avg `-0.0175` n `18`; unknown avg `0.0965` n `547`
- 4h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.75` n `228`; crypto_major avg `-0.9424` n `8`; equity avg `-0.1419` n `74`; fx avg `0.2262` n `6`; index avg `0.2183` n `23`; metal avg `0.023` n `18`; unknown avg `-0.066` n `545`
- 24h: commodity avg `-1.2338` n `12`; crypto_alt avg `-0.8279` n `228`; crypto_major avg `-0.0996` n `8`; equity avg `2.1108` n `74`; fx avg `0.0978` n `6`; index avg `1.1655` n `23`; metal avg `0.8633` n `18`; unknown avg `-2.8685` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
