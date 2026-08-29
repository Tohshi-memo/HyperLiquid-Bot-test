# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T05:22:23.286124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0085` n `231`; crypto_major avg `-0.0141` n `8`; equity avg `-0.0035` n `127`; fx avg `0.001` n `6`; index avg `0.0091` n `26`; metal avg `-0.005` n `20`; unknown avg `-0.0444` n `793`
- 1h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.2787` n `231`; crypto_major avg `0.2238` n `8`; equity avg `0.0145` n `127`; fx avg `0.0132` n `6`; index avg `0.0222` n `26`; metal avg `0.0105` n `20`; unknown avg `0.142` n `793`
- 4h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.1832` n `231`; crypto_major avg `0.3222` n `8`; equity avg `0.114` n `127`; fx avg `0.023` n `6`; index avg `0.0582` n `26`; metal avg `0.026` n `20`; unknown avg `-0.175` n `793`
- 24h: commodity avg `-0.1458` n `12`; crypto_alt avg `-1.2077` n `231`; crypto_major avg `-1.899` n `8`; equity avg `-1.5485` n `127`; fx avg `-0.0673` n `6`; index avg `-0.1231` n `26`; metal avg `-0.2282` n `20`; unknown avg `-0.3367` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
