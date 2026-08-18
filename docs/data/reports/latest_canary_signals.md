# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T12:07:28.957775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `0.0372` n `230`; crypto_major avg `0.0008` n `8`; equity avg `-0.0152` n `114`; fx avg `-0.0005` n `6`; index avg `-0.0003` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0771` n `795`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `0.0585` n `230`; crypto_major avg `0.1344` n `8`; equity avg `0.0229` n `114`; fx avg `0.0087` n `6`; index avg `0.0069` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.0226` n `795`
- 4h: commodity avg `0.0112` n `12`; crypto_alt avg `0.4626` n `230`; crypto_major avg `0.426` n `8`; equity avg `-0.0286` n `114`; fx avg `-0.0148` n `6`; index avg `0.0221` n `25`; metal avg `0.0398` n `20`; unknown avg `-0.0325` n `795`
- 24h: commodity avg `0.6623` n `12`; crypto_alt avg `-0.692` n `230`; crypto_major avg `0.2293` n `8`; equity avg `-2.2544` n `114`; fx avg `-0.0424` n `6`; index avg `-0.4847` n `25`; metal avg `-0.1838` n `20`; unknown avg `-0.0746` n `760`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
