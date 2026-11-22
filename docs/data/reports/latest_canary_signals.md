# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T03:22:24.483005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0135` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0165` n `13`; crypto_alt avg `0.0307` n `239`; crypto_major avg `0.0182` n `8`; equity avg `-0.0209` n `166`; fx avg `-0.0056` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0222` n `20`; unknown avg `-0.2132` n `1261`
- 1h: commodity avg `-0.0388` n `13`; crypto_alt avg `-0.6186` n `239`; crypto_major avg `-0.6885` n `8`; equity avg `-0.2041` n `166`; fx avg `0.0033` n `6`; index avg `-0.0618` n `27`; metal avg `-0.0803` n `20`; unknown avg `161.771` n `1261`
- 4h: commodity avg `-0.0668` n `13`; crypto_alt avg `-1.0367` n `239`; crypto_major avg `-1.0867` n `8`; equity avg `-0.3223` n `166`; fx avg `-0.0144` n `6`; index avg `-0.0732` n `27`; metal avg `-0.0934` n `20`; unknown avg `177.7207` n `1252`
- 24h: commodity avg `-0.0424` n `13`; crypto_alt avg `0.4454` n `239`; crypto_major avg `2.1063` n `8`; equity avg `0.5995` n `166`; fx avg `-0.0462` n `6`; index avg `0.1176` n `27`; metal avg `0.0361` n `20`; unknown avg `418.3253` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
