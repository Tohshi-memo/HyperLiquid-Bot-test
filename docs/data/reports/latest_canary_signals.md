# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T02:07:27.407200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `-0.0053` n `230`; crypto_major avg `-0.0672` n `8`; equity avg `-0.2283` n `107`; fx avg `-0.013` n `6`; index avg `-0.0415` n `25`; metal avg `-0.0513` n `20`; unknown avg `-0.0685` n `780`
- 1h: commodity avg `0.0161` n `12`; crypto_alt avg `0.484` n `230`; crypto_major avg `0.5623` n `8`; equity avg `0.656` n `107`; fx avg `0.0174` n `6`; index avg `0.1624` n `25`; metal avg `0.1398` n `20`; unknown avg `-0.1037` n `780`
- 4h: commodity avg `0.1948` n `12`; crypto_alt avg `0.1522` n `230`; crypto_major avg `0.3156` n `8`; equity avg `-0.1402` n `107`; fx avg `-0.0508` n `6`; index avg `-0.0106` n `25`; metal avg `0.1335` n `20`; unknown avg `-0.2674` n `780`
- 24h: commodity avg `0.2065` n `12`; crypto_alt avg `1.0363` n `230`; crypto_major avg `0.9308` n `8`; equity avg `1.4796` n `107`; fx avg `-0.0431` n `6`; index avg `0.1084` n `25`; metal avg `-0.0951` n `20`; unknown avg `0.2538` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
