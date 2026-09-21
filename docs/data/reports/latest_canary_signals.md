# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T04:37:26.896150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `0.1689` n `234`; crypto_major avg `0.0833` n `8`; equity avg `-0.0582` n `140`; fx avg `0.0184` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0212` n `20`; unknown avg `1.7496` n `944`
- 1h: commodity avg `0.0727` n `12`; crypto_alt avg `0.3209` n `234`; crypto_major avg `-0.1416` n `8`; equity avg `-0.0203` n `140`; fx avg `0.0362` n `6`; index avg `0.0131` n `26`; metal avg `-0.0075` n `20`; unknown avg `54.6748` n `936`
- 4h: commodity avg `-0.1683` n `12`; crypto_alt avg `0.2017` n `234`; crypto_major avg `-0.5902` n `8`; equity avg `-0.0541` n `140`; fx avg `-0.0039` n `6`; index avg `0.044` n `26`; metal avg `-0.0026` n `20`; unknown avg `54.9137` n `935`
- 24h: commodity avg `-0.6128` n `12`; crypto_alt avg `3.3765` n `234`; crypto_major avg `2.3255` n `8`; equity avg `1.0594` n `140`; fx avg `0.0006` n `6`; index avg `0.2136` n `26`; metal avg `0.0638` n `20`; unknown avg `4.794` n `763`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
