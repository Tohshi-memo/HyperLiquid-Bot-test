# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T11:00:29.936339+00:00`
- Correlation status: `ready`
- Asset price records: `259`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0573` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0031` n `7`; crypto_alt avg `-0.1219` n `223`; crypto_major avg `-0.1253` n `7`; equity avg `0.0385` n `42`; fx avg `-0.008` n `4`; index avg `-0.0263` n `9`; metal avg `0.1473` n `7`; unknown avg `0.2945` n `314`
- 1h: commodity avg `0.4491` n `7`; crypto_alt avg `-1.4383` n `223`; crypto_major avg `-1.2752` n `7`; equity avg `-0.6362` n `42`; fx avg `-0.0121` n `4`; index avg `-0.2179` n `9`; metal avg `-0.3235` n `7`; unknown avg `-0.2062` n `314`
- 4h: commodity avg `0.5378` n `7`; crypto_alt avg `-0.9851` n `223`; crypto_major avg `-1.081` n `7`; equity avg `-0.7436` n `42`; fx avg `-0.0193` n `4`; index avg `-0.4988` n `9`; metal avg `-1.0424` n `7`; unknown avg `0.2092` n `314`
- 24h: commodity avg `1.0287` n `7`; crypto_alt avg `1.1795` n `223`; crypto_major avg `0.9828` n `7`; equity avg `0.1581` n `42`; fx avg `-0.067` n `4`; index avg `0.3921` n `9`; metal avg `-1.4784` n `7`; unknown avg `0.2996` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.29`, n `255`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2825`, n `255`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2401`, n `251`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2392`, n `251`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2102`, n `251`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.2019`, n `255`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1963`, n `251`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1892`, n `255`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1865`, n `251`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `255`, weak_sample_signal
