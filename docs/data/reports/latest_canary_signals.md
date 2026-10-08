# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T12:07:30.379358+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1425` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0644` n `13`; crypto_alt avg `-0.3436` n `235`; crypto_major avg `-0.2274` n `8`; equity avg `-0.0197` n `150`; fx avg `0.0212` n `6`; index avg `0.0066` n `26`; metal avg `0.0175` n `20`; unknown avg `-0.2923` n `1069`
- 1h: commodity avg `-0.0445` n `13`; crypto_alt avg `-0.2331` n `235`; crypto_major avg `-0.3263` n `8`; equity avg `0.1625` n `150`; fx avg `0.0137` n `6`; index avg `0.0613` n `26`; metal avg `0.0814` n `20`; unknown avg `0.2119` n `1069`
- 4h: commodity avg `0.2569` n `13`; crypto_alt avg `-0.6141` n `235`; crypto_major avg `-1.1694` n `8`; equity avg `-0.297` n `150`; fx avg `0.0247` n `6`; index avg `-0.0269` n `26`; metal avg `-0.09` n `20`; unknown avg `2.3724` n `1069`
- 24h: commodity avg `0.7739` n `13`; crypto_alt avg `0.0537` n `235`; crypto_major avg `-2.1935` n `8`; equity avg `-1.3326` n `150`; fx avg `0.0704` n `6`; index avg `-0.1958` n `26`; metal avg `-0.1166` n `20`; unknown avg `416.4736` n `974`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
