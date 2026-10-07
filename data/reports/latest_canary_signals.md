# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T08:22:37.219323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0738` n `13`; crypto_alt avg `-0.0699` n `235`; crypto_major avg `-0.0347` n `8`; equity avg `0.0197` n `150`; fx avg `0.0192` n `6`; index avg `0.0145` n `26`; metal avg `-0.0179` n `20`; unknown avg `-0.0653` n `1076`
- 1h: commodity avg `0.03` n `13`; crypto_alt avg `-0.2396` n `235`; crypto_major avg `-0.1293` n `8`; equity avg `-0.153` n `150`; fx avg `-0.0737` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0293` n `20`; unknown avg `0.0109` n `1058`
- 4h: commodity avg `0.0765` n `13`; crypto_alt avg `0.3414` n `235`; crypto_major avg `0.4018` n `8`; equity avg `-0.2821` n `150`; fx avg `-0.1175` n `6`; index avg `-0.0522` n `26`; metal avg `-0.1647` n `20`; unknown avg `0.1209` n `1036`
- 24h: commodity avg `0.7669` n `13`; crypto_alt avg `-3.4562` n `235`; crypto_major avg `-2.1591` n `8`; equity avg `-0.4353` n `149`; fx avg `-0.0771` n `6`; index avg `-0.1211` n `26`; metal avg `-0.2592` n `20`; unknown avg `814.702` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
