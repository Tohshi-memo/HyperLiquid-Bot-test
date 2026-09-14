# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T13:07:31.165371+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `-0.5657` n `233`; crypto_major avg `-0.5202` n `8`; equity avg `-0.2025` n `136`; fx avg `-0.0099` n `6`; index avg `-0.0507` n `27`; metal avg `-0.0391` n `20`; unknown avg `1.177` n `892`
- 1h: commodity avg `0.1133` n `12`; crypto_alt avg `-0.9845` n `233`; crypto_major avg `-0.7017` n `8`; equity avg `-0.3144` n `136`; fx avg `0.0065` n `6`; index avg `-0.0818` n `27`; metal avg `-0.1123` n `20`; unknown avg `96.5768` n `886`
- 4h: commodity avg `0.067` n `12`; crypto_alt avg `-1.0082` n `233`; crypto_major avg `-0.5749` n `8`; equity avg `-0.6014` n `136`; fx avg `0.0512` n `6`; index avg `-0.0931` n `27`; metal avg `-0.189` n `20`; unknown avg `4.827` n `886`
- 24h: commodity avg `0.5948` n `12`; crypto_alt avg `-0.8288` n `233`; crypto_major avg `1.0553` n `8`; equity avg `-1.3183` n `136`; fx avg `0.0753` n `6`; index avg `-0.2913` n `27`; metal avg `-0.511` n `20`; unknown avg `1.1468` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
