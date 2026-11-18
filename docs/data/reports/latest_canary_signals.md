# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T15:22:54.907138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0232` n `13`; crypto_alt avg `0.0082` n `239`; crypto_major avg `-0.0753` n `8`; equity avg `0.0218` n `164`; fx avg `-0.0084` n `6`; index avg `0.0044` n `27`; metal avg `0.0013` n `20`; unknown avg `0.2329` n `1263`
- 1h: commodity avg `-0.1597` n `13`; crypto_alt avg `-0.3033` n `239`; crypto_major avg `-0.6508` n `8`; equity avg `-0.5336` n `164`; fx avg `-0.0072` n `6`; index avg `-0.0184` n `27`; metal avg `-0.1672` n `20`; unknown avg `5.2137` n `1263`
- 4h: commodity avg `-0.0059` n `13`; crypto_alt avg `-0.4717` n `239`; crypto_major avg `-0.8852` n `8`; equity avg `-1.1736` n `164`; fx avg `-0.0214` n `6`; index avg `-0.1115` n `27`; metal avg `-0.1249` n `20`; unknown avg `0.8808` n `1257`
- 24h: commodity avg `-0.182` n `13`; crypto_alt avg `-0.4972` n `239`; crypto_major avg `-0.9805` n `8`; equity avg `0.1191` n `164`; fx avg `-0.1476` n `6`; index avg `0.0338` n `27`; metal avg `-1.1908` n `20`; unknown avg `-0.2338` n `1136`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
