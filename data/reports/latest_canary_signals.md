# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T21:22:24.951322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.255` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `-0.4244` n `229`; crypto_major avg `-0.5535` n `8`; equity avg `-0.1764` n `91`; fx avg `-0.012` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0079` n `20`; unknown avg `0.168` n `763`
- 1h: commodity avg `0.142` n `12`; crypto_alt avg `-0.4422` n `229`; crypto_major avg `-0.5419` n `8`; equity avg `-0.0868` n `91`; fx avg `-0.0061` n `6`; index avg `-0.0138` n `25`; metal avg `-0.0575` n `20`; unknown avg `0.0455` n `763`
- 4h: commodity avg `0.4402` n `12`; crypto_alt avg `-1.5762` n `229`; crypto_major avg `-1.3728` n `8`; equity avg `-0.7204` n `91`; fx avg `-0.0099` n `6`; index avg `-0.1178` n `25`; metal avg `-0.3791` n `20`; unknown avg `0.5458` n `761`
- 24h: commodity avg `1.0257` n `12`; crypto_alt avg `-2.8968` n `229`; crypto_major avg `-2.3878` n `8`; equity avg `-3.3278` n `91`; fx avg `-0.2424` n `6`; index avg `-0.6287` n `25`; metal avg `-0.6156` n `20`; unknown avg `-0.4667` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
