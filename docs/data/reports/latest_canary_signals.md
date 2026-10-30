# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T23:07:29.671617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0363` n `13`; crypto_alt avg `0.1494` n `238`; crypto_major avg `0.0843` n `8`; equity avg `0.0499` n `156`; fx avg `-0.0026` n `6`; index avg `0.0012` n `27`; metal avg `-0.0028` n `20`; unknown avg `0.4831` n `1255`
- 1h: commodity avg `-0.055` n `13`; crypto_alt avg `0.5986` n `238`; crypto_major avg `0.2964` n `8`; equity avg `0.0766` n `156`; fx avg `0.0014` n `6`; index avg `0.0035` n `27`; metal avg `0.0067` n `20`; unknown avg `0.7703` n `1255`
- 4h: commodity avg `-0.3313` n `13`; crypto_alt avg `1.7659` n `238`; crypto_major avg `0.6279` n `8`; equity avg `1.1228` n `156`; fx avg `-0.0427` n `6`; index avg `0.1206` n `27`; metal avg `0.1154` n `20`; unknown avg `1.4912` n `1149`
- 24h: commodity avg `0.0648` n `13`; crypto_alt avg `1.918` n `238`; crypto_major avg `-0.6133` n `8`; equity avg `-2.5308` n `156`; fx avg `-0.162` n `6`; index avg `-0.2191` n `27`; metal avg `-0.9046` n `20`; unknown avg `1.0557` n `1014`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
