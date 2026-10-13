# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T06:52:30.162325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.028` n `235`; crypto_major avg `0.0138` n `8`; equity avg `-0.016` n `151`; fx avg `-0.0237` n `6`; index avg `0.0358` n `26`; metal avg `0.0662` n `20`; unknown avg `-0.0372` n `1135`
- 1h: commodity avg `-0.0376` n `13`; crypto_alt avg `0.1345` n `235`; crypto_major avg `0.1566` n `8`; equity avg `-0.1832` n `151`; fx avg `-0.0204` n `6`; index avg `0.0265` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.2381` n `1117`
- 4h: commodity avg `-0.0425` n `13`; crypto_alt avg `2.4074` n `235`; crypto_major avg `1.2805` n `8`; equity avg `0.5283` n `151`; fx avg `0.0198` n `6`; index avg `0.1208` n `26`; metal avg `0.156` n `20`; unknown avg `1.3594` n `1075`
- 24h: commodity avg `0.3469` n `13`; crypto_alt avg `-3.4452` n `235`; crypto_major avg `-2.0623` n `8`; equity avg `-3.4822` n `151`; fx avg `0.009` n `6`; index avg `-0.4477` n `26`; metal avg `-0.0467` n `20`; unknown avg `0.4403` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.196`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1785`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1517`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.129`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0932`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0818`, n `666`, weak_sample_signal
