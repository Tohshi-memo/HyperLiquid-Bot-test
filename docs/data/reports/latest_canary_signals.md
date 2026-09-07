# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T03:37:26.056362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1232` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `-0.3708` n `232`; crypto_major avg `-0.2815` n `8`; equity avg `-0.0014` n `134`; fx avg `-0.0118` n `6`; index avg `0.0151` n `26`; metal avg `-0.0196` n `20`; unknown avg `-0.2299` n `794`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `-0.5581` n `232`; crypto_major avg `-0.7755` n `8`; equity avg `-0.0594` n `134`; fx avg `0.0231` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0918` n `20`; unknown avg `0.0801` n `764`
- 4h: commodity avg `0.0052` n `12`; crypto_alt avg `-1.0627` n `232`; crypto_major avg `-1.1063` n `8`; equity avg `0.2554` n `134`; fx avg `-0.0218` n `6`; index avg `0.0169` n `26`; metal avg `-0.0821` n `20`; unknown avg `2.8942` n `756`
- 24h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.3164` n `232`; crypto_major avg `-0.9238` n `8`; equity avg `0.333` n `134`; fx avg `0.0206` n `6`; index avg `0.003` n `26`; metal avg `-0.1598` n `20`; unknown avg `74.2656` n `650`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1959`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
