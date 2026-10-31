# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T05:07:26.527091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0109` n `238`; crypto_major avg `0.1555` n `8`; equity avg `0.0402` n `156`; fx avg `-0.0037` n `6`; index avg `0.0072` n `27`; metal avg `0.0078` n `20`; unknown avg `0.146` n `1256`
- 1h: commodity avg `-0.0257` n `13`; crypto_alt avg `-0.4133` n `238`; crypto_major avg `-0.2047` n `8`; equity avg `-0.06` n `156`; fx avg `-0.009` n `6`; index avg `-0.0101` n `27`; metal avg `0.0055` n `20`; unknown avg `-0.1003` n `1256`
- 4h: commodity avg `0.1341` n `13`; crypto_alt avg `-1.0317` n `238`; crypto_major avg `-0.6626` n `8`; equity avg `-0.1301` n `156`; fx avg `-0.0069` n `6`; index avg `-0.0555` n `27`; metal avg `-0.0093` n `20`; unknown avg `-0.3612` n `1232`
- 24h: commodity avg `0.0129` n `13`; crypto_alt avg `1.0572` n `238`; crypto_major avg `-1.5809` n `8`; equity avg `-2.8751` n `156`; fx avg `-0.0901` n `6`; index avg `-0.2342` n `27`; metal avg `-0.6771` n `20`; unknown avg `4.0152` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
