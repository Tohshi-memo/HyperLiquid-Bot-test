# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T16:07:29.810786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.4108` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0422` n `13`; crypto_alt avg `0.0016` n `239`; crypto_major avg `-0.1273` n `8`; equity avg `0.258` n `164`; fx avg `-0.0086` n `6`; index avg `0.0399` n `27`; metal avg `-0.0019` n `20`; unknown avg `2.6436` n `1253`
- 1h: commodity avg `-0.0463` n `13`; crypto_alt avg `-0.6322` n `239`; crypto_major avg `-0.7933` n `8`; equity avg `-0.5895` n `164`; fx avg `-0.0225` n `6`; index avg `-0.0668` n `27`; metal avg `-0.0672` n `20`; unknown avg `-0.6882` n `1255`
- 4h: commodity avg `-0.152` n `13`; crypto_alt avg `-1.1109` n `239`; crypto_major avg `-1.5637` n `8`; equity avg `-1.6632` n `164`; fx avg `-0.0236` n `6`; index avg `-0.1529` n `27`; metal avg `-0.2845` n `20`; unknown avg `0.9179` n `1255`
- 24h: commodity avg `-0.4268` n `13`; crypto_alt avg `-0.2019` n `239`; crypto_major avg `-0.4976` n `8`; equity avg `0.4172` n `164`; fx avg `-0.1895` n `6`; index avg `0.0648` n `27`; metal avg `-1.2178` n `20`; unknown avg `-0.5006` n `1138`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
