# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T05:52:29.631518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0425` n `13`; crypto_alt avg `0.1896` n `237`; crypto_major avg `0.0629` n `8`; equity avg `0.1336` n `151`; fx avg `-0.0076` n `6`; index avg `0.0326` n `26`; metal avg `-0.0371` n `20`; unknown avg `0.6142` n `1198`
- 1h: commodity avg `0.0317` n `13`; crypto_alt avg `-0.151` n `237`; crypto_major avg `-0.2856` n `8`; equity avg `-0.2173` n `151`; fx avg `-0.0113` n `6`; index avg `-0.0085` n `26`; metal avg `-0.1194` n `20`; unknown avg `-0.2478` n `1196`
- 4h: commodity avg `0.0227` n `13`; crypto_alt avg `0.2107` n `237`; crypto_major avg `0.0702` n `8`; equity avg `-0.5335` n `151`; fx avg `-0.0032` n `6`; index avg `-0.1025` n `26`; metal avg `0.046` n `20`; unknown avg `0.1516` n `1188`
- 24h: commodity avg `0.292` n `13`; crypto_alt avg `0.0966` n `237`; crypto_major avg `-0.6034` n `8`; equity avg `-1.4692` n `151`; fx avg `0.0085` n `6`; index avg `-0.2371` n `26`; metal avg `-0.3651` n `20`; unknown avg `5.392` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
