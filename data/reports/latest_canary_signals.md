# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T05:22:28.294998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3233` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0134` n `12`; crypto_alt avg `-0.1538` n `234`; crypto_major avg `-0.0957` n `8`; equity avg `-0.0245` n `140`; fx avg `-0.0049` n `6`; index avg `0.0015` n `26`; metal avg `0.0025` n `20`; unknown avg `1.2596` n `943`
- 1h: commodity avg `-0.0354` n `12`; crypto_alt avg `0.0451` n `234`; crypto_major avg `0.1313` n `8`; equity avg `-0.0176` n `140`; fx avg `-0.0033` n `6`; index avg `-0.0051` n `26`; metal avg `0.0098` n `20`; unknown avg `18.3696` n `931`
- 4h: commodity avg `0.129` n `12`; crypto_alt avg `-1.5485` n `234`; crypto_major avg `-1.3988` n `8`; equity avg `-0.4284` n `140`; fx avg `-0.0124` n `6`; index avg `-0.0755` n `26`; metal avg `-0.0349` n `20`; unknown avg `5.1442` n `925`
- 24h: commodity avg `0.221` n `12`; crypto_alt avg `-0.5078` n `234`; crypto_major avg `-1.9472` n `8`; equity avg `-0.2469` n `140`; fx avg `-0.0478` n `6`; index avg `-0.0379` n `26`; metal avg `-0.0011` n `20`; unknown avg `4.7346` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
