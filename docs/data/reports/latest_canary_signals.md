# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T19:37:20.380881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0918` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.043` n `12`; crypto_alt avg `-0.1215` n `228`; crypto_major avg `-0.1495` n `8`; equity avg `-0.005` n `69`; fx avg `-0.0014` n `6`; index avg `0.0847` n `23`; metal avg `-0.0127` n `18`; unknown avg `-0.0354` n `421`
- 1h: commodity avg `-0.067` n `12`; crypto_alt avg `-0.2145` n `228`; crypto_major avg `-0.2535` n `8`; equity avg `0.0439` n `69`; fx avg `-0.0063` n `6`; index avg `0.2105` n `23`; metal avg `-0.0096` n `18`; unknown avg `0.0037` n `421`
- 4h: commodity avg `0.0426` n `12`; crypto_alt avg `-0.5762` n `228`; crypto_major avg `-0.7149` n `8`; equity avg `0.0456` n `69`; fx avg `-0.0101` n `6`; index avg `0.3769` n `23`; metal avg `-0.0335` n `18`; unknown avg `-0.1164` n `421`
- 24h: commodity avg `0.6457` n `12`; crypto_alt avg `-1.4033` n `228`; crypto_major avg `-0.9594` n `8`; equity avg `0.8503` n `69`; fx avg `-0.0248` n `6`; index avg `0.3235` n `23`; metal avg `-0.1302` n `18`; unknown avg `0.3015` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2496`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
