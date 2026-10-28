# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T10:22:34.133366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0236` n `13`; crypto_alt avg `0.0419` n `238`; crypto_major avg `0.1199` n `8`; equity avg `0.2328` n `154`; fx avg `-0.0026` n `6`; index avg `0.0307` n `27`; metal avg `-0.0219` n `20`; unknown avg `0.5503` n `1237`
- 1h: commodity avg `0.0837` n `13`; crypto_alt avg `0.1465` n `238`; crypto_major avg `0.2554` n `8`; equity avg `0.0789` n `154`; fx avg `0.0027` n `6`; index avg `0.0025` n `27`; metal avg `-0.1109` n `20`; unknown avg `0.8712` n `1218`
- 4h: commodity avg `0.0001` n `13`; crypto_alt avg `0.3847` n `238`; crypto_major avg `0.7337` n `8`; equity avg `0.2054` n `154`; fx avg `0.0303` n `6`; index avg `0.0199` n `27`; metal avg `-0.0202` n `20`; unknown avg `94.9992` n `1184`
- 24h: commodity avg `-0.1252` n `13`; crypto_alt avg `3.1082` n `238`; crypto_major avg `3.3325` n `8`; equity avg `3.7797` n `154`; fx avg `0.0831` n `6`; index avg `0.5061` n `27`; metal avg `0.3233` n `20`; unknown avg `7.1755` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1795`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
