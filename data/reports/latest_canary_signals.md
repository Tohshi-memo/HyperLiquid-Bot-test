# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T14:03:46.073690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0381` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.4738` n `232`; crypto_major avg `0.3657` n `8`; equity avg `0.1178` n `134`; fx avg `-0.0041` n `6`; index avg `-0.0273` n `26`; metal avg `0.0314` n `20`; unknown avg `0.6436` n `781`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.7457` n `232`; crypto_major avg `-0.5404` n `8`; equity avg `-0.0358` n `134`; fx avg `0.0039` n `6`; index avg `-0.0988` n `26`; metal avg `-0.1112` n `20`; unknown avg `1.3854` n `781`
- 4h: commodity avg `-0.2415` n `12`; crypto_alt avg `-1.4814` n `232`; crypto_major avg `-1.0665` n `8`; equity avg `0.3026` n `134`; fx avg `0.0092` n `6`; index avg `-0.0284` n `26`; metal avg `-0.0489` n `20`; unknown avg `0.8863` n `775`
- 24h: commodity avg `-0.0837` n `12`; crypto_alt avg `-1.1404` n `232`; crypto_major avg `-1.4275` n `8`; equity avg `0.2021` n `134`; fx avg `-0.1431` n `6`; index avg `-0.0887` n `26`; metal avg `0.038` n `20`; unknown avg `7061.7632` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
