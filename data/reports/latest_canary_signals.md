# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T02:07:28.045752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `13`; crypto_alt avg `0.0361` n `239`; crypto_major avg `-0.0199` n `8`; equity avg `-0.0224` n `166`; fx avg `-0.0072` n `6`; index avg `-0.0053` n `27`; metal avg `-0.0204` n `20`; unknown avg `2.0691` n `1252`
- 1h: commodity avg `0.0025` n `13`; crypto_alt avg `0.0105` n `239`; crypto_major avg `-0.0478` n `8`; equity avg `-0.1017` n `166`; fx avg `-0.0018` n `6`; index avg `-0.0143` n `27`; metal avg `-0.038` n `20`; unknown avg `0.3483` n `1258`
- 4h: commodity avg `-0.0523` n `13`; crypto_alt avg `-0.2372` n `239`; crypto_major avg `-0.2194` n `8`; equity avg `0.5796` n `166`; fx avg `-0.0353` n `6`; index avg `0.0687` n `27`; metal avg `-0.0017` n `20`; unknown avg `1.3626` n `1234`
- 24h: commodity avg `0.3201` n `13`; crypto_alt avg `-3.83` n `239`; crypto_major avg `-4.5168` n `8`; equity avg `-4.6737` n `166`; fx avg `-0.0217` n `6`; index avg `-0.5145` n `27`; metal avg `-0.0852` n `20`; unknown avg `16.9076` n `1113`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
