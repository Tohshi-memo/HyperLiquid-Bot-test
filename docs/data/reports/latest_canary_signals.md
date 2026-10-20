# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T01:37:28.796049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0105` n `13`; crypto_alt avg `0.2949` n `237`; crypto_major avg `0.1802` n `8`; equity avg `0.1462` n `151`; fx avg `0.0047` n `6`; index avg `0.0707` n `26`; metal avg `0.0139` n `20`; unknown avg `0.3522` n `1198`
- 1h: commodity avg `0.1037` n `13`; crypto_alt avg `-0.1647` n `237`; crypto_major avg `-0.1525` n `8`; equity avg `-0.3054` n `151`; fx avg `0.008` n `6`; index avg `-0.0395` n `26`; metal avg `-0.126` n `20`; unknown avg `-0.2778` n `1196`
- 4h: commodity avg `0.1326` n `13`; crypto_alt avg `0.0785` n `237`; crypto_major avg `-0.2498` n `8`; equity avg `-0.9053` n `151`; fx avg `-0.0273` n `6`; index avg `-0.1347` n `26`; metal avg `-0.1937` n `20`; unknown avg `0.1014` n `1178`
- 24h: commodity avg `0.2381` n `13`; crypto_alt avg `-0.386` n `237`; crypto_major avg `-0.5272` n `8`; equity avg `-0.7257` n `151`; fx avg `-0.0345` n `6`; index avg `-0.078` n `26`; metal avg `-0.3684` n `20`; unknown avg `5.0836` n `1012`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
