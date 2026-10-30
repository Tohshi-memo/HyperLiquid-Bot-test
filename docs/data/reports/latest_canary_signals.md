# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T13:22:28.755453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `13`; crypto_alt avg `-0.0405` n `238`; crypto_major avg `0.0765` n `8`; equity avg `0.0609` n `156`; fx avg `-0.0115` n `6`; index avg `0.0166` n `27`; metal avg `0.099` n `20`; unknown avg `2.2325` n `1257`
- 1h: commodity avg `-0.0947` n `13`; crypto_alt avg `-0.1416` n `238`; crypto_major avg `-0.1911` n `8`; equity avg `-0.0911` n `156`; fx avg `-0.0468` n `6`; index avg `0.0246` n `27`; metal avg `-0.0287` n `20`; unknown avg `63.1833` n `1251`
- 4h: commodity avg `-0.0934` n `13`; crypto_alt avg `0.4314` n `238`; crypto_major avg `-0.1086` n `8`; equity avg `-0.9455` n `156`; fx avg `-0.0886` n `6`; index avg `-0.0882` n `27`; metal avg `-0.3128` n `20`; unknown avg `1.8608` n `1247`
- 24h: commodity avg `0.5168` n `13`; crypto_alt avg `-4.4961` n `238`; crypto_major avg `-3.2727` n `8`; equity avg `-4.2997` n `156`; fx avg `0.0587` n `6`; index avg `-0.4352` n `27`; metal avg `-0.8086` n `20`; unknown avg `3449.285` n `1036`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
