# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T11:22:25.857964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.1405` n `230`; crypto_major avg `0.0939` n `8`; equity avg `0.0105` n `112`; fx avg `0.0108` n `6`; index avg `-0.0101` n `25`; metal avg `-0.1152` n `20`; unknown avg `0.0032` n `782`
- 1h: commodity avg `-0.071` n `12`; crypto_alt avg `0.0591` n `230`; crypto_major avg `0.2071` n `8`; equity avg `0.2113` n `112`; fx avg `0.0065` n `6`; index avg `0.0344` n `25`; metal avg `-0.067` n `20`; unknown avg `-0.0491` n `782`
- 4h: commodity avg `-0.2969` n `12`; crypto_alt avg `0.189` n `230`; crypto_major avg `0.8843` n `8`; equity avg `0.5597` n `112`; fx avg `-0.0274` n `6`; index avg `0.0462` n `25`; metal avg `0.0356` n `20`; unknown avg `0.1723` n `782`
- 24h: commodity avg `0.176` n `12`; crypto_alt avg `0.7213` n `230`; crypto_major avg `0.3826` n `8`; equity avg `2.4067` n `109`; fx avg `-0.0921` n `6`; index avg `0.1063` n `25`; metal avg `0.2474` n `20`; unknown avg `0.3772` n `765`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
