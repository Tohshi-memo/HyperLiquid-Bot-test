# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T22:37:27.445143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `0.0962` n `235`; crypto_major avg `0.0385` n `8`; equity avg `-0.018` n `151`; fx avg `-0.0015` n `6`; index avg `0.0124` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.1704` n `1135`
- 1h: commodity avg `0.0898` n `13`; crypto_alt avg `-0.9299` n `235`; crypto_major avg `-0.6843` n `8`; equity avg `-0.0515` n `151`; fx avg `0.0107` n `6`; index avg `0.0228` n `26`; metal avg `0.0066` n `20`; unknown avg `0.6017` n `1117`
- 4h: commodity avg `-0.1301` n `13`; crypto_alt avg `-0.9537` n `235`; crypto_major avg `-0.4219` n `8`; equity avg `0.0282` n `151`; fx avg `-0.0012` n `6`; index avg `0.0175` n `26`; metal avg `0.0507` n `20`; unknown avg `0.6153` n `1060`
- 24h: commodity avg `0.2796` n `13`; crypto_alt avg `-4.042` n `235`; crypto_major avg `-2.4515` n `8`; equity avg `-3.5074` n `151`; fx avg `-0.1495` n `6`; index avg `-0.3388` n `26`; metal avg `-0.0846` n `20`; unknown avg `0.1135` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2035`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1762`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1107`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0867`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0861`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0754`, n `666`, weak_sample_signal
