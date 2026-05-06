# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T02:30:29.312921+00:00`
- Correlation status: `ready`
- Asset price records: `414`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.1732` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1128` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0188` n `7`; crypto_alt avg `-0.3613` n `223`; crypto_major avg `-0.3224` n `7`; equity avg `0.014` n `47`; fx avg `0.0097` n `4`; index avg `-0.0532` n `6`; metal avg `-0.1132` n `7`; unknown avg `-0.0356` n `313`
- 1h: commodity avg `-0.1431` n `7`; crypto_alt avg `0.1107` n `223`; crypto_major avg `-0.1721` n `7`; equity avg `0.1348` n `47`; fx avg `0.0042` n `4`; index avg `-0.0745` n `6`; metal avg `0.1109` n `7`; unknown avg `-0.1043` n `313`
- 4h: commodity avg `-0.5918` n `7`; crypto_alt avg `0.285` n `223`; crypto_major avg `-0.5551` n `7`; equity avg `0.3742` n `47`; fx avg `-0.2616` n `4`; index avg `0.5577` n `6`; metal avg `1.6181` n `7`; unknown avg `-0.1638` n `313`
- 24h: commodity avg `-1.5021` n `7`; crypto_alt avg `1.9635` n `223`; crypto_major avg `1.7827` n `7`; equity avg `2.6451` n `47`; fx avg `-0.1858` n `4`; index avg `2.199` n `6`; metal avg `1.5429` n `7`; unknown avg `1.0078` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1851`, n `410`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1788`, n `410`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `410`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `410`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `410`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.104`, n `410`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1012`, n `406`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `410`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `410`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0954`, n `406`, weak_sample_signal
