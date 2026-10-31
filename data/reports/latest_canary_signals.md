# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T22:36:46.411261+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `13`; crypto_alt avg `-0.0507` n `238`; crypto_major avg `-0.0078` n `8`; equity avg `-0.0032` n `156`; fx avg `-0.0012` n `6`; index avg `0.0082` n `27`; metal avg `0.0045` n `20`; unknown avg `0.1469` n `1260`
- 1h: commodity avg `0.0424` n `13`; crypto_alt avg `0.0151` n `238`; crypto_major avg `0.1476` n `8`; equity avg `0.0246` n `156`; fx avg `-0.0018` n `6`; index avg `0.0093` n `27`; metal avg `0.0166` n `20`; unknown avg `5.6834` n `1166`
- 4h: commodity avg `0.0346` n `13`; crypto_alt avg `-0.3402` n `238`; crypto_major avg `-0.1018` n `8`; equity avg `-0.0039` n `156`; fx avg `-0.0054` n `6`; index avg `-0.0079` n `27`; metal avg `0.017` n `20`; unknown avg `1.495` n `1110`
- 24h: commodity avg `-0.0382` n `13`; crypto_alt avg `-0.2812` n `238`; crypto_major avg `0.1875` n `8`; equity avg `0.2041` n `156`; fx avg `0.0056` n `6`; index avg `-0.0419` n `27`; metal avg `0.0524` n `20`; unknown avg `1.1712` n `1049`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
